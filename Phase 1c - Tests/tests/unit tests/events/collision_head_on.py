from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Airport, Plane
import mock
import datetime

NOW = datetime.datetime.now()

"""
for plane_1 in list_planes()

    for plane_2 in list_planes()
    
        if plane_1.airport_origin is plane_2.airport_destination

        and plane_1.airport_destination is plane_2.airport_origin

            return head on collision
"""


class Fake:
    def __init__(self):
        self.planes = {
            plane0 = Plane(id=0, size="small", speed=1, 
                                airport_dest=0, airport_src=3, 
                                dt_depart=NOW, dt_arrival=NOW + 1,
                                currentPassengerCount=0, maxPassengerCount=500),

            plane1 = Plane(id=1, size="small", speed=1, 
                                airport_dest=3, airport_src=0, 
                                dt_depart=NOW, dt_arrival=NOW + 1,
                                currentPassengerCount=0, maxPassengerCount=500),

            plane0 = Plane(id=0, size="small", speed=1, 
                                airport_dest=0, airport_src=1, 
                                dt_depart=NOW, dt_arrival=NOW + 1,
                                currentPassengerCount=0, maxPassengerCount=500),

            plane1 = Plane(id=1, size="small", speed=1, 
                                airport_dest=2, airport_src=3, 
                                dt_depart=NOW, dt_arrival=NOW + 1,
                                currentPassengerCount=0, maxPassengerCount=500),
            }

        def getPlane(id)
            return self.planes.get(id=id)


def fake_planes():
    return lambda: Fake.planes


@mock.patch("classes.models.Plane")
class UnitTestCases(TestCase):
    def test_headon_FAIL(self, mock_plane):
        mock_plane.get.side_effect = Fake.fake_planes()
        self.assertEqual(Fake.getPlane(0).no_headon(), False) # this plane will not avoid a headon

    def test_headon_PASS(self, mock_plane):
        mock_plane.get.side_effect = Fake.fake_planes()
        self.assertEqual(Fake.getPlane(3).no_headon(), True) # this plane will avoid a headon