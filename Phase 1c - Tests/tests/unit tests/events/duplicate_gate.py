from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Gate, Plane
import mock
import datetime

NOW = datetime.datetime.now()

"""
    Plane.check_gate(gate_id, plane_eta) should:
        -   check db junection table for query filter matches and
        -   return True if gate_id is available at given plane_eta time, else return False

"""


class Junct:
    def __init__(self, gate_id, plane_id, dt_available):
        self.gate_id = gate_id
        self.plane_id = plane_id
        self.dt_available = dt_available


class FakeGates:
    def __init__(self):
        self.gates = {
            Junct(gate_id=1, plane_id=1, dt_available=NOW),
            Junct(gate_id=2, plane_id=2, dt_available=NOW),
            }

    def checkGate(self, gate_id, plane_eta):
        return self.gates.filter(gate_id=gate_id).filter(dt_available__lt=plane_eta)


plane = Plane(id=1, size="small",
                    currentPassengerCount=0, maxPassengerCount=500)


@mock.patch("classes.models.Plane")
class UnitTestCases(TestCase):

    def test_assign_FAIL(self, mock_plane):
        mock_plane.check_gate.side_effect = FakeGates.checkGate(2, NOW - 1)
        self.assertEqual(plane.check_gate(1), False) # FAIL, since gate is not avaialable yet

    def test_assign_PASS(self, mock_plane):
        mock_plane.check_gate.side_effect = FakeGates.checkGate(2, NOW + 1)
        self.assertEqual(plane.check_gate(1), True) # PASS, since gate is avaialable then
