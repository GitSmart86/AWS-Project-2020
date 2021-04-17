from atc.models import Airport, Airline, Gate, Runway, Plane
from atc.helpers import all_air_collisions, find_duplicate_gate, find_duplicate_runway
from json import dumps, loads
from dateutil import parser
from django.core.management.base import BaseCommand
import pulsar
import pytz
import traceback

utc = pytz.UTC

# Use lemurs for production environment
# TEAM_ID = 'lemurs'
# Use team-a for development environment

TEAM_ID = 'lemurs'

PULSAR_SERVER = 'pulsar://pulsar.bjucps.dev:6650'


class Command(BaseCommand):
    help = 'processes entries in the pulsar queue'

    def handle(self, *args, **options):
        client = pulsar.Client(PULSAR_SERVER)
        consumer = client.subscribe(
            'events', subscription_name=TEAM_ID, consumer_type=pulsar.ConsumerType.Shared)
        try:

            # Use WHILE for production environment
            # while True:
            while True:
                # Use FOR for developement environment
                msg = consumer.receive(timeout_millis=5000)

                # process message
                try:
                    # body is a dictionary converted from json
                    body = loads(msg.data())

                    if "speed" in body:
                        # duplicate logic found in plane view's update method
                        # call all_air_collisions in the helpers.py file
                        plane = Plane.objects.filter(
                            identifier=body["plane"]).first()
                        direction = float(body["direction"])
                        speed = float(body["speed"])
                        origin = Airport.objects.filter(
                            name=body["origin"]).first()
                        destination = Airport.objects.filter(
                            name=body["destination"]).first()
                        take_off_time = utc.localize(
                            parser.parse(body["take_off_time"]))
                        landing_time = utc.localize(
                            parser.parse(body["landing_time"]))

                        plane.take_off_airport = origin
                        plane.land_airport = destination
                        plane.take_off_time = take_off_time
                        plane.landing_time = landing_time
                        plane.heading = direction
                        plane.speed = speed
                        plane.runway = None
                        plane.save()

                        all_air_collisions(plane)

                    elif "gate" in body:
                        # duplicate logic found in gate view's assignment method
                        # call find_duplicate_gates in helpers.py file
                        plane = Plane.objects.filter(
                            identifier=body["plane"]).first()
                        gate = Gate.objects.filter(
                            identifier=body["gate"]).first()

                        if "arrive_at_time" in body:
                            date = utc.localize(
                                parser.parse(body["arrive_at_time"]))
                            plane.arrive_at_gate_time = date
                        else:  # if there is no arriave at time, then we are at the gate
                            plane.arrive_at_gate_time = None
                            plane.runway = None  # if we are at the gate then we are not at the runway
                        plane.save()

                        find_duplicate_gate(plane)

                    elif "runway" in body:
                        # duplicate logic found in runway view's assignment method
                        # call find duplicate runway in helpers.py file
                        plane = Plane.objects.filter(
                            identifier=body["plane"]).first()
                        runway = Runway.objects.filter(
                            identifier=body["runway"]).first()

                        plane.runway = runway
                        if "arrive_at_time" in body:
                            date = utc.localize(
                                parser.parse(body["arrive_at_time"]))
                            plane.arrive_at_runway_time = date
                            plane.save()
                        else:  # if there is no arriave at time, then we are at the game
                            plane.arrive_at_runway_time = None
                            plane.gate = None
                            plane.heading = 0
                            plane.speed = 0
                            plane.take_off_airport = plane.land_airport
                            plane.land_airport = None
                            plane.take_off_time = None
                            plane.landing_time = None
                        plane.save()

                        find_duplicate_runway(plane)
                except Exception as e:
                    print(e)
                    traceback.print_exc()
                finally:
                    # only acknowledge message if you want to consume the message on Pulsar
                    consumer.acknowledge(msg)
        except TimeoutError:
            pass
        except Exception as e:
            print(e)
            traceback.print_exc()
        finally:
            client.close()
