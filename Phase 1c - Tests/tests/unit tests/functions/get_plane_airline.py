from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Plane, Airline
import mock


def has_airline(doesHave: bool):
    return Airline(id=1, name="test") if doesHave else None


@mock.patch("classes.models.Plane")
class UnitTestCases(TestCase):

    def test_get_plane_airline(self, mock_Gate):
        plane1 = Plane(id="1", size="small")
        mock_Gate.getPlane.side_effect = has_airline(True)
        self.assertEqual(plane1.getplane(), not None)

    def test_get_plane_airline_Null(self, mock_Gate):
        plane1 = Plane(id="1", size="small")
        mock_Gate.getPlane.side_effect = has_airline(True)

        if plane1.getAirline() is None:
            # This test should fail. Every plane must have a parent airline.
            self.assertEqual(True, False)
