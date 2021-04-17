from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Plane, Gate
import mock


def has_gate(doesHave: bool):
    return Gate(id=1, size="small") if doesHave else None


@mock.patch("classes.models.Plane")
class UnitTestCases(TestCase):

    def test_get_plane_gate(self, mock_Gate):
        plane1 = Plane(id="1", size="small")
        mock_Gate.getPlane.side_effect = has_gate(True)
        self.assertEqual(plane1.getGate(), not None)

    def test_get_plane_gate_Null(self, mock_Gate):
        plane1 = Plane(id="1", size="small")
        mock_Gate.getGate.side_effect = has_gate(False)
        self.assertEqual(plane1.getGate(), None)
