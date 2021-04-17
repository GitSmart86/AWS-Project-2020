from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Runway, Plane
import mock

"""
use django model validators

    Plane.setRunway(runway_id) should:
        -   try to insert a (plane_id, runway_id, dt_arrival) entry into the respective db junction table
        -   return True if db accepts, else False

"""


class Junct:
    def __init__(self, id, size):
        self.size = size
        self.id = id


class FakeRunways:
    def __init__(self):
        self.runways = {
            Junct(id=1, size="small"),
            Junct(id=2, size="medium"),
            Junct(id=3, size="large"),
        }

    def getPlane(self, gate_id):
        return self.runways.get(gate_id=gate_id)


def fake_runway(runway_id: int):
    return lambda: FakeRunways.getRunway(runway_id)


plane_small = Plane(id=1,
                    size="small",
                    currentPassengerCount=0,
                    maxPassengerCount=500)

plane_large = Plane(id=2,
                    size="large",
                    currentPassengerCount=0,
                    maxPassengerCount=500)


@mock.patch("classes.models.Runway")
class UnitTestCases(TestCase):

    def test_too_small_runway(self, mock_plane):
        mock_plane.fetchRunway.side_effect = fake_runway(1)
        self.assertEqual(plane_large.setRunway(1), False)

    def test_large_runway(self, mock_datetime):
        mock_plane.fetchRunway.side_effect = fake_runway(2)
        self.assertEqual(plane_small.setRunway(2), True)

    def test_equal_runway(self, mock_datetime):
        mock_plane.fetchRunway.side_effect = fake_runway(3)
        self.assertEqual(plane_large.setRunway(3), True)
