from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Gate, Plane
import mock

"""
use django model validators

    Plane.setGate(gate_id) should:
        -   try to insert a (plane_id, gate_id, dt_arrival) entry into the respective db junction table
        -   return True if db accepts, else False

"""


class Junct:
    def __init__(self, id, size):
        self.size = size
        self.id = id


class FakeGates:
    def __init__(self):
        self.gates = {
            Junct(id=1, size="small"),
            Junct(id=2, size="medium"),
            Junct(id=3, size="large"),
        }

    def getPlane(self, gate_id):
        return self.gates.get(gate_id=gate_id)


def fake_gate(gate_id: int):
    return lambda: FakeGates.getGate(gate_id)


plane_small = Plane(id=1,
                    size="small",
                    currentPassengerCount=0,
                    maxPassengerCount=500)

plane_large = Plane(id=2,
                    size="large",
                    currentPassengerCount=0,
                    maxPassengerCount=500)


@mock.patch("classes.models.Gate")
class UnitTestCases(TestCase):

    def test_too_small_Gate(self, mock_plane):
        mock_plane.fetchGate.side_effect = fake_gate(1)
        self.assertEqual(plane_large.setGate(1), False)

    def test_large_Gate(self, mock_datetime):
        mock_plane.fetchGate.side_effect = fake_gate(2)
        self.assertEqual(plane_small.setGate(2), True)

    def test_equal_Gate(self, mock_datetime):
        mock_plane.fetchGate.side_effect = fake_gate(3)
        self.assertEqual(plane_large.setGate(3), True)
