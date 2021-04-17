from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Runway, Airport
import mock


def has_airport(doesHave: bool):
    return Airport(id=1, name="test", x=1, y=1) if doesHave else None


@mock.patch("classes.models.Runway")
class UnitTestCases(TestCase):

    def test_get_runway_airport(self, mock_Airport):
        runway1 = Runway(id="1", size="small")
        mock_Airport.getAirport.side_effect = has_airport(True)
        self.assertEqual(runway1.getAirport(), not None)

    def test_get_runway_airport_Null(self, mock_Airport):
        runway1 = Runway(id="1", size="small")
        mock_Airport.getAirport.side_effect = has_airport(True)

        if runway1.getAirport() is None:
            # This test should fail. Every plane must have a parent airline.
            self.assertEqual(True, False)
