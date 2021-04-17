from django.db.models import Q
from .models import Plane, Airport
from math import sqrt, degrees, atan2
from datetime import timedelta
import requests
import json
import pulsar


def calc_distance(origin_airport: Airport, dest_airport: Airport):
    return sqrt((dest_airport.x - origin_airport.x)**2 + (dest_airport.y - origin_airport.y)**2)


def calc_heading(origin_airport: Airport, dest_airport: Airport):
    theta = degrees(atan2(origin_airport.x - dest_airport.x,
                          dest_airport.y - origin_airport.y))
    return (theta + 90) % 360


def get_intersection_point(plane1: Plane, plane2: Plane):
    x1 = plane1.take_off_airport.x
    x2 = plane1.land_airport.x
    x3 = plane2.take_off_airport.x
    x4 = plane2.land_airport.x
    y1 = plane1.take_off_airport.y
    y2 = plane1.land_airport.y
    y3 = plane2.take_off_airport.y
    y4 = plane2.land_airport.y
    return (((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)),
            ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)))


def calc_distance_with_tuple(origin_airport: Airport, dest: tuple):
    return sqrt((dest[0] - origin_airport.x)**2 + (dest[1] - origin_airport.y)**2)


def arrive_at_intersection_at_same_minute(plane1: Plane, plane2: Plane):
    try:
        intersection_point = get_intersection_point(plane1, plane2)
        p1dist = calc_distance_with_tuple(
            plane1.take_off_airport, intersection_point)
        p2dist = calc_distance_with_tuple(
            plane2.take_off_airport, intersection_point)
        p1arrive = plane1.take_off_time + \
            timedelta(hours=p1dist / plane1.speed)
        p2arrive = plane2.take_off_time + \
            timedelta(hours=p2dist / plane2.speed)
        print(p1arrive - p2arrive)
        # are the times within 60 seconds
        return abs((p1arrive - p2arrive).total_seconds()) <= 60
    except Exception as e:
        print(e)
        return False


def all_air_collisions(launchingPlane: Plane):
    planes = []

    # find planes with opposite airports of the launchingPlane and overlapping take off / landing times
    planes += Plane.objects.filter(take_off_airport=launchingPlane.land_airport,
                                   land_airport=launchingPlane.take_off_airport).all()

    # find planes with same airports of the launchingPlane and overlapping take off / landing times
    planes += Plane.objects.filter(take_off_airport=launchingPlane.take_off_airport, land_airport=launchingPlane.land_airport,
                                   landing_time__gt=launchingPlane.landing_time, take_off_time__lt=launchingPlane.take_off_time).all()

    # find planes that can potentially intersect with the launchPlane, then see if they arrive at the same time
    temp = Plane.objects.exclude(Q(take_off_airport=launchingPlane.land_airport, land_airport=launchingPlane.take_off_airport) | Q(
        take_off_airport=launchingPlane.take_off_airport, land_airport=launchingPlane.land_airport)).exclude(landing_time=None).all()
    for cPlane in temp:
        if arrive_at_intersection_at_same_minute(launchingPlane, cPlane):
            planes.append(cPlane)

    for plane in planes:
        send_imminent_collision_post(
            launchingPlane.identifier, "COLLISION_IMMINENT")
        send_imminent_collision_post(plane.identifier, "COLLISION_IMMINENT")


def send_imminent_collision_post(identifier, error):
    err = error
    txt = {
        "team_id": "89ecdb63-8123-4ded-a647-5f7409a9cfc5",
        "obj_type": "PLANE",
        "id": identifier,
        "error": err
    }
    print(f"sending_warning... {error}")
    client = pulsar.Client('pulsar://pulsar.bjucps.dev:6650')
    producer = client.create_producer('warnings')
    producer.send(json.dumps(txt).encode('utf-8'))
    client.close()

    # url = "https://evently.bjucps.dev/app/error_report"
    # x = requests.post(url, data=json.loads(txt))
    # return x


def find_duplicate_runway(landingPlane: Plane):
    planes = []

    # find planes with the same runway (and no arrive at gate time)
    planes += Plane.objects.filter(runway=landingPlane.runway,
                                   arrive_at_gate_time=None, take_off_time=None).all()
    # find planes with the same runway (and an arrive at gate time or take off time that is after our arrive at runway time)
    planes += Plane.objects.filter(runway=landingPlane.runway).filter(
        Q(arrive_at_gate_time__gt=landingPlane.arrive_at_runway_time) | Q(take_off_time=landingPlane.arrive_at_runway_time)).all()

    for plane in planes:
        send_imminent_collision_post(
            landingPlane.identifier, "DUPLICATE_RUNWAY")
        send_imminent_collision_post(plane.identifier, "DUPLICATE_RUNWAY")


def find_duplicate_gate(arrivingPlane: Plane):
    planes = []

    # find planes with the same gate (and no arrive at runway time)
    planes += Plane.objects.filter(gate=arrivingPlane.gate,
                                   arrive_at_runway_time=None).all()
    # find planes with the same gate (and an arrive at runway time that is after our arrive at game time)
    planes += Plane.objects.filter(gate=arrivingPlane.gate,
                                   arrive_at_runway_time__gt=arrivingPlane.arrive_at_gate_time).all()

    for plane in planes:
        send_imminent_collision_post(
            arrivingPlane.identifier, "DUPLICATE_GATE")
        send_imminent_collision_post(plane.identifier, "DUPLICATE_GATE")
