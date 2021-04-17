from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Plane, Airline
import mock


class Junct:
    def __init__(self, airline_id, plane_id):
        self.plane_id = plane_id
        self.airline_id = airline_id


class FakePlanes:
    def __init__(self):
        self.planes = {
            Junct(airline_id=1, plane_id=1),
            Junct(airline_id=2, plane_id=1),
            Junct(airline_id=3, plane_id=2),
            Junct(airline_id=4, plane_id=2),
            Junct(airline_id=5, plane_id=3),
        }

    def getPlanes(self, airline_id):
        return self.planes.filter(airline_id=airline_id)


class UnitTestCases(TestCase):
    @mock.patch("classes.models.Airline")
    def test_list_planes(self, mock_planes):
        airline1 = Airline(id=1, name="test")
        mock_planes.getPlanes.side_effect = FakePlanes.getPlanes(airline1.id)
        self.assertEqual(airline1.getPlanes(), not None)

    @mock.patch("classes.models.Airline")
    def test_list_planes_Null(self, mock_planes):
        airline1 = Airline(id=4, name="test")
        mock_planes.getPlanes.side_effect = FakePlanes.getPlanes(airline1.id)
        self.assertEqual(airline1.getPlanes(), None)
