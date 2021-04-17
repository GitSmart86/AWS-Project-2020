from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Plane, Runway
import mock


def has_plane(doesHave: bool):
    return Plane(id=1, size="small", currentPassengerCount=5, maxPassengerCount=500) if doesHave else None


@mock.patch("classes.models.Runway")
class UnitTestCases(TestCase):

    def test_get_runway_plane(self, mock_Plane):
        runway1 = Runway(id="1", size="small")
        mock_Gate.getPlane.side_effect = has_plane(True)
        self.assertEqual(runway1.getPlane(), not None)

    def test_get_runway_plane_Null(self, mock_Plane):
        runway1 = Runway(id="1", size="small")
        mock_Gate.getPlane.side_effect = has_plane(False)
        self.assertEqual(runway1.getPlane(), None)
