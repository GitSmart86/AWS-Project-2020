from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Gate, Plane
import mock


def has_plane(doesHave: bool):
    return Plane(id=1, size="small", currentPassengerCount=5, maxPassengerCount=500) if doesHave else None


@mock.patch("classes.models.Gate")
class UnitTestCases(TestCase):

    def test_get_gate_plane(self, mock_Gate):
        gate1 = Gate(id="1", size="small")
        mock_Gate.getPlane.side_effect = has_plane(True)
        self.assertEqual(gate1.getplane(), not None)

    def test_get_gate_plane_Null(self, mock_Gate):
        gate1 = Gate(id="1", size="small")
        mock_Gate.getPlane.side_effect = has_plane(False)
        self.assertEqual(gate1.getplane(), None)
