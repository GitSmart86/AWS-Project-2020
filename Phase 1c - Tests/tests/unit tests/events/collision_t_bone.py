from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Airport, Plane
import mock
import datetime

NOW = datetime.datetime.now()

"""
DEFINTION: T-Bone Collision = 2 planes inhabbit the same 5 square miles within the same datetime minute.

NOTE: each plane will have a flight_path dictionary attribute of [ DT_minute : (x,y) ]

NOTE: in plane_gate_launch(...), the flight_path dictionary will be calculated for the given plane's upcoming flight

for plane_1 in list_planes()

    for plane_2 in list_planes()

        for DT_minute in plane_1.flight_path[]

            if plane_2.flight_path[DT_minute].exists()

                if abs( plane_1.flight_path[DT_minute].getX() 
                        - plane_2.flight_path[DT_minute].getX() 
                       ) <= 5
                
                and abs( plane_1.flight_path[DT_minute].getY() 
                         - plane_2.flight_path[DT_minute].getY() 
                        ) <= 5

                    return t-bone collision alert


    NOTE:   IF Progamming wants to use this optional method above,
                this test will likely not pass, 
                    until the predicted inflight dt_minute_(x,y) table is filled out.
            After Programming creates the function that will calculate the needed dt_minute_(x,y) table for each plane,
                could Programming please send Architecture sample table data for these 4 planes' coordinates?
                    Then, Architecture can add the tables to their respective planes in this test,
                        so that these two tests can PASS.
"""


class Fake:
    def __init__(self):
        self.planes = {
            plane0 = Plane(id=0, size="small", speed=1, 
                                airport_dest=0, airport_src=3, 
                                dt_depart=NOW, dt_arrival=NOW + 1,
                                currentPassengerCount=0, maxPassengerCount=500),

            plane1 = Plane(id=1, size="small", speed=1, 
                                airport_dest=1, airport_src=2, 
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

        self.airports = {
            airport00 = Airport(id=0, name="0", x=0, y=0),
            airport01 = Airport(id=1, name="0", x=0, y=10),
            airport10 = Airport(id=2, name="0", x=10, y=0),
            airport11 = Airport(id=3, name="1", x=10, y=10),
            }

        def getPlane(id)
            return self.planes.get(id=id)


def fake_planes():
    return lambda: Fake.planes

def fake_airports():
    return lambda: Fake.airports


@mock.patch("classes.models.Plane")
@mock.patch("classes.models.Airport")
class UnitTestCases(TestCase):
    def test_tbone_FAIL(self, mock_plane, mock_airport):
        mock_plane.get.side_effect = Fake.fake_planes()
        mock_airport.get.side_effect = Fake.fake_airports()
        self.assertEqual(Fake.getPlane(0).no_tbone(), False) # this plane will not avoid a tbone

    def test_tbone_PASS(self, mock_plane, mock_airport):
        mock_plane.get.side_effect = Fake.fake_planes()
        mock_airport.get.side_effect = Fake.fake_airports()
        self.assertEqual(Fake.getPlane(3).no_tbone(), True) # this plane will avoid a tbone
