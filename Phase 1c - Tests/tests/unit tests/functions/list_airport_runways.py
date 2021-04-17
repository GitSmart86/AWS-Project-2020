from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Runway, Airport
import mock


class Junct:
    def __init__(self, airport_id, runway_id):
        self.runway_id = runway_id
        self.airport_id = airport_id

    # def get(self):
    #     return None

# def fake_datetime(day: int):
#     return lambda: FakeNow(day)


class FakeRunways:
    def __init__(self):
        self.runways = {
            Junct(runway_id=1, airport_id=1),
            Junct(runway_id=2, airport_id=1),
            Junct(runway_id=3, airport_id=2),
            Junct(runway_id=4, airport_id=2),
            Junct(runway_id=5, airport_id=3)
        }

    def getRunways(self, airport_id):
        return self.runways.filter(airport_id=airport_id)


class UnitTestCases(TestCase):
    @mock.patch("classes.models.Airport")
    def test_list_runways(self, mock_runways):
        airport1 = Airport(id=1, name="test", x=1, y=1)
        mock_airlines.getRunways.side_effect = FakeRunways.getRunways(
            airport1.id)
        self.assertEqual(airport1.getRunways(), not None)

    @mock.patch("classes.models.Airport")
    def test_list_runways_Null(self, mock_runways):
        airport1 = Airport(id=1, name="test", x=1, y=1)
        mock_airlines.getRunways.side_effect = FakeRunways.getRunways(
            airport1.id)
        self.assertEqual(airport1.getRunways(), None)
