from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Plane, Runway
import mock


def has_Runway(doesHave: bool):
    return Runway(id=1, size="small") if doesHave else None


@mock.patch("classes.models.Plane")
class UnitTestCases(TestCase):

    def test_get_plane_runway(self, mock_Runway):
        plane1 = Plane(id="1", size="small")
        mock_Runway.getRunway.side_effect = has_Runway(True)
        self.assertEqual(plane1.getRunway(), not None)

    def test_get_plane_runway_Null(self, mock_Runway):
        plane1 = Plane(id="1", size="small")
        mock_Runway.getRunway.side_effect = has_Runway(False)
        self.assertEqual(plane1.getRunway(), None)
