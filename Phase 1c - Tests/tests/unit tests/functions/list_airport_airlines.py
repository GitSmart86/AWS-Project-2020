from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Airline, Airport
import mock


class Junct:
    def __init__(self, airport_id, airline_id):
        self.airline_id = airline_id
        self.airport_id = airport_id


class FakeAirlines:
    def __init__(self):
        self.airlines = {
            Junct(airline_id=1, airport_id=1),
            Junct(airline_id=2, airport_id=1),
            Junct(airline_id=3, airport_id=2),
            Junct(airline_id=4, airport_id=2),
            Junct(airline_id=5, airport_id=3)
        }

    def getAirlines(self, airport_id):
        return self.airlines.filter(airport_id=airport_id)


class UnitTestCases(TestCase):
    @mock.patch("classes.models.Airport")
    def test_list_airlines(self, mock_airlines):
        airport1 = Airport(id=1, name="test", x=1, y=1)
        mock_airlines.getAirlines.side_effect = FakeAirlines.getAirlines(
            airport1.id)
        self.assertEqual(airport1.getAirlines(), not None)

    @mock.patch("classes.models.Airport")
    def test_list_airlines_Null(self, mock_airlines):
        airport1 = Airport(id=1, name="test", x=1, y=1)
        mock_airlines.getAirlines.side_effect = FakeAirlines.getAirlines(
            airport1.id)
        self.assertEqual(airport1.getAirlines(), None)
