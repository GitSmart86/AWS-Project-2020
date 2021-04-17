from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Plane
import mock

"""
use django model validators

    Plane.set_Occupancy_Current(occupancy) should:
        -   try to set self.occupancy_current to variable value and compare agains self.occupancy_limit
        -   return True if current < limit, else False

"""


class UnitTestCases(TestCase):

    def test_set_plane_occupancy_FAIL(self, mock_plane):
        plane_small = Plane(id=1,
                            size="small",
                            currentPassengerCount=0,
                            maxPassengerCount=50)
        self.assertEqual(plane_small.setOccupancy(400), False)
        self.assertEqual(plane_small.Occupancy_Current, 0)

    def test_set_plane_occupancy_PASS(self, mock_plane):
        plane_large = Plane(id=1,
                            size="large",
                            currentPassengerCount=0,
                            maxPassengerCount=500)
        self.assertEqual(plane_large.setOccupancy(400), True)
        self.assertEqual(plane_large.Occupancy_Current, 400)
