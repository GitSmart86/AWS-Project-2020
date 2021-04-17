from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Gate, Airport
import mock


class Junct:
    def __init__(self, airport_id, gate_id):
        self.gate_id = gate_id
        self.airport_id = airport_id


class FakeGates:
    def __init__(self):
        self.gates = {
            Junct(gate_id=1, airport_id=1),
            Junct(gate_id=2, airport_id=1),
            Junct(gate_id=3, airport_id=2),
            Junct(gate_id=4, airport_id=2),
            Junct(gate_id=5, airport_id=3),
        }

    def getGates(self, airport_id):
        return self.gates.filter(airport_id=airport_id)


class UnitTestCases(TestCase):
    @mock.patch("classes.models.Airport")
    def test_list_gates(self, mock_gates):
        airport1 = Airport(id=1, name="test", x=1, y=1)
        mock_airlines.getGates.side_effect = FakeGates.getGates(airport1.id)
        self.assertEqual(airport1.getGates(), not None)

    @mock.patch("classes.models.Airport")
    def test_list_gates_Null(self, mock_gates):
        airport1 = Airport(id=1, name="test", x=1, y=1)
        mock_airlines.getGates.side_effect = FakeGates.getGates(airport1.id)
        self.assertEqual(airport1.getGates(), None)
