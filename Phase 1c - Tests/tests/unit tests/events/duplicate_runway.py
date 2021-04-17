from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Runway, Plane
import mock
import datetime

NOW = datetime.datetime.now()

"""
    Plane.check_runway(runway_id, plane_eta) should:
        -   check db junection table for query filter matches and
        -   return True if runway_id is available at given plane_eta time, else return False

"""


class Junct:
    def __init__(self, plane_id, runway_id, dt_available):
        self.runway_id = runway_id
        self.plane_id = plane_id
        self.dt_available = dt_available


class FakeRunways:
    def __init__(self):
        self.runways = {
            Junct(runway_id=1, plane_id=1, dt_available=NOW),
            Junct(runway_id=2, plane_id=2, dt_available=NOW),
            }

    def checkRunway(self, runway_id, plane_eta):
        return self.runways.filter(runway_id=runway_id).filter(dt_available__lt=plane_eta)


plane = Plane(id=1, size="small",
                    currentPassengerCount=0, maxPassengerCount=500)


@mock.patch("classes.models.Plane")
class UnitTestCases(TestCase):

    def test_assign_FAIL(self, mock_plane):
        mock_plane.check_runway.side_effect = FakeGates.checkRunway(2, NOW - 1)
        self.assertEqual(plane.check_runway(1), False) # FAIL, since gate is not avaialable yet

    def test_assign_PASS(self, mock_plane):
        mock_plane.check_runway.side_effect = FakeGates.checkRunway(2, NOW + 1)
        self.assertEqual(plane.check_runway(1), True) # PASS, since gate is avaialable then
