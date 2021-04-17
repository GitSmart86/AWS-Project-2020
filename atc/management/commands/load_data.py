import csv
from atc.models import Airport, Airline, Gate, Runway, Plane
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'loads data into database if needed'

    def handle(self, *args, **options):
        loadedAirports = False
        loadedAirlines = False

        if Airport.objects.count() == 0:
            loadedAirports = True
            with open("atc/data/airport.csv") as file:
                reader = csv.DictReader(file)
                for airport in reader:
                    Airport.objects.create(
                        name=airport["name"],
                        x=float(airport["x"]),
                        y=float(airport["y"])
                    )
            print("airports loaded")
        else:
            print("airports already loaded")

        if Airline.objects.count() == 0:
            loadedAirlines = True
            with open("atc/data/airline.csv") as file:
                reader = csv.DictReader(file)
                for airline in reader:
                    Airline.objects.create(name=airline["name"])
            print("airlines loaded")
        else:
            print("airlines already loaded")

        if loadedAirports or loadedAirlines:
            with open("atc/data/airport_airline.csv") as file:
                reader = csv.DictReader(file)
                for combo in reader:
                    Airport.objects.get(
                        name=combo["airport"]
                    ).airlines.add(
                        Airline.objects.get(name=combo["airline"])
                    )
            print("airport / airlines loaded")
        else:
            print("airport / airlines already loaded")

        if Gate.objects.count() == 0:
            with open("atc/data/gate.csv") as file:
                reader = csv.DictReader(file)
                for gate in reader:
                    Gate.objects.create(
                        identifier=gate["id"],
                        airport=Airport.objects.get(name=gate["airport"]),
                        size=gate["size"]
                    )
            print("gates loaded")
        else:
            print("gates already loaded")

        if Runway.objects.count() == 0:
            with open("atc/data/runway.csv") as file:
                reader = csv.DictReader(file)
                for runway in reader:
                    Runway.objects.create(
                        identifier=runway["id"],
                        airport=Airport.objects.get(name=runway["airport"]),
                        size=runway["size"]
                    )
            print("runways loaded")
        else:
            print("runways already loaded")

        if Plane.objects.count() == 0:
            with open("atc/data/plane.csv") as file:
                reader = csv.DictReader(file)
                for plane in reader:
                    Plane.objects.create(
                        identifier=plane["id"],
                        airline=Airline.objects.get(name=plane["airline"]),
                        size=plane["size"],
                        currentPassengerCount=0,
                        maxPassengerCount=plane["maxPassenger"]
                    )
            print("planes loaded")
        else:
            print("planes already loaded")