from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Gate, Airport
import mock


def has_airport(doesHave: bool):
    return Airport(id=1, name="test", x=1, y=1) if doesHave else None


@mock.patch("classes.models.Gate")
class UnitTestCases(TestCase):

    def test_get_gate_airport(self, mock_Gate):
        gate1 = Gate(id="1", size="small")
        mock_Gate.getAirport.side_effect = has_airport(True)
        self.assertEqual(gate1.getAirport(), not None)

    def test_get_gate_airport_Null(self, mock_Gate):
        gate1 = Gate(id="1", size="small")
        mock_Gate.getAirport.side_effect = has_airport(True)

        if gate1.getAirport() is None:
            # This test should fail. Every gate must have a parent airport.
            self.assertEqual(True, False)
