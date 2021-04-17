from django.test import Client, TestCase
from atc.models import Airline, Airport, Gate, Runway, Plane
from django.contrib.auth.models import User
from unittest.mock import patch
from datetime import datetime, timedelta
from django.core import management
import json
from atc.helpers import calc_heading, calc_distance

# less than 400 indicates success of some sort
class AirportTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='temporary', email='temporary@gmail.com', password='temporary')

    def test_airport_create_edit_delete(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        response = c.post('/atc/airports/create/', {'name': 'ATL', 'x': '0.0', 'y': '0.0'})
        self.assertLess(response.status_code, 400)
        airport = Airport.objects.get(name='ATL')
        self.assertIsNotNone(airport)
        self.assertEqual(airport.x, 0.0)
        self.assertEqual(airport.y, 0.0)

        response = c.post(f'/atc/airports/{airport.id}/update/', {'name': 'ATL', 'x': '1.0', 'y': '1.0'})
        self.assertLess(response.status_code, 400)
        airport = Airport.objects.get(name='ATL')
        self.assertEqual(airport.x, 1.0)
        self.assertEqual(airport.y, 1.0)

        response = c.post(f'/atc/airports/{airport.id}/delete/')
        try:
            airport = Airport.objects.get(name='ATL')
            self.assertTrue(True, False) # we should not have gotten here
        except Airport.DoesNotExist:
            pass

        # cleanup
        Airport.objects.all().delete()

    def test_airport_create_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # airport with same name creation
        Airport.objects.create(name='ATL', x=0.0, y=0.0)
        response = c.post('/atc/airports/create/', {'name': 'ATL', 'x': '0.0', 'y': '0.0'})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # cleanup
        Airport.objects.all().delete()

    def test_airport_update_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # airport with same name during update
        airport1 = Airport.objects.create(name='ATL', x=0.0, y=0.0)
        Airport.objects.create(name='ATL2', x=0.0, y=0.0)
        response = c.post(f'/atc/airports/{airport1.id}/update/', {'name': 'ATL2', 'x': '0.0', 'y': '0.0'})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # cleanup
        Airport.objects.all().delete()

    def test_airport_delete_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # delete non existent airport
        response = c.post(f'/atc/airports/1/delete/')
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

class AirlineTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='temporary', email='temporary@gmail.com',
                                                  password='temporary')

    def test_airline_create_edit_delete(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # dependencies: Airport
        response = c.post('/atc/airports/create/', {'name': 'Airline Test Airport', 'x': 1.0, 'y': 1.0})
        self.assertLess(response.status_code, 400)
        airport = Airport.objects.get(name='Airline Test Airport')

        response = c.post('/atc/airlines/create/', {'name': 'Delta', 'airports': [airport.id]})
        self.assertLess(response.status_code, 400)
        airline = Airline.objects.get(name='Delta')
        self.assertIsNotNone(airline)
        self.assertEqual(airline.airport_set.count(), 1)

        response = c.post(f'/atc/airlines/{airline.id}/update/', {'name': 'Delta 2', 'airports': [airport.id]})
        self.assertLess(response.status_code, 400)
        try:
            airline = Airline.objects.get(name='Delta')
            self.assertTrue(True, False) # we should not have gotten here
        except Airline.DoesNotExist:
            pass
        airline = Airline.objects.get(name='Delta 2')
        self.assertIsNotNone(airline)
        self.assertEqual(airline.airport_set.count(), 1)

        response = c.post(f'/atc/airlines/{airline.id}/delete/')
        self.assertLess(response.status_code, 400)
        try:
            airline = Airline.objects.get(name='Delta 2')
            self.assertTrue(True, False)  # we should not have gotten here
        except Airline.DoesNotExist:
            pass

        # cleanup
        Airline.objects.all().delete()
        Airport.objects.all().delete()

    def test_airline_create_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # airline with same name creation
        Airline.objects.create(name='Delta')
        response = c.post('/atc/airlines/create/', {'name': 'Delta'})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # cleanup
        Airline.objects.all().delete()

    def test_airline_update_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # airline with same name during update
        airline1 = Airline.objects.create(name='Delta')
        Airline.objects.create(name='Delta2')
        response = c.post(f'/atc/airlines/{airline1.id}/update/', {'name': 'Delta2'})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # cleanup
        Airline.objects.all().delete()

    def test_airline_delete_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # delete non existent airline
        response = c.post(f'/atc/airlines/1/delete/')
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

class GateTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='temporary', email='temporary@gmail.com',
                                                  password='temporary')

    def test_gate_create_edit_delete(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # dependencies: Airport
        response = c.post('/atc/airports/create/', {'name': 'Gate Test Airport', 'x': '0.0', 'y': '0.0'})
        self.assertLess(response.status_code, 400)
        airport = Airport.objects.get(name='Gate Test Airport')

        response = c.post('/atc/gates/create/', {'identifier': 'G1', 'size': 'SMALL', 'airport': airport.id})
        self.assertLess(response.status_code, 400)
        gate = Gate.objects.get(identifier='G1')
        self.assertIsNotNone(gate)
        self.assertEqual(gate.size, 'SMALL')
        self.assertEqual(gate.airport, airport)

        response = c.post(f'/atc/gates/{gate.id}/update/', {'identifier': 'G1', 'size': 'MEDIUM', 'airport': airport.id})
        self.assertLess(response.status_code, 400)
        gate = Gate.objects.get(identifier='G1')
        self.assertIsNotNone(gate)
        self.assertEqual(gate.size, 'MEDIUM')
        self.assertEqual(gate.airport, airport)
        response = c.post(f'/atc/gates/{gate.id}/delete/')
        self.assertLess(response.status_code, 400)
        try:
            gate = Gate.objects.get(identifier='G1')
            self.assertTrue(True, False) # we should not have gotten here
        except Gate.DoesNotExist:
            pass

        # cleanup
        Gate.objects.all().delete()
        Airport.objects.all().delete()

    def test_gate_create_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # gate with same name creation
        airport = Airport.objects.create(name='Gate Test Airport', x=0.0, y=0.0)
        Gate.objects.create(identifier='G1', size='SMALL', airport=airport)
        response = c.post('/atc/gates/create/', {'identifier': 'G1', 'size': 'SMALL', 'airport': airport.id})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)
        # gate with invalid size
        response = c.post('/atc/gates/create/', {'identifier': 'G2', 'size': 'TANGO', 'airport': airport.id})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # cleanup
        Gate.objects.all().delete()
        Airport.objects.all().delete()

    def test_gate_update_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # gate with same name during update
        airport = Airport.objects.create(name='Gate Test Airport', x=0.0, y=0.0)
        gate1 = Gate.objects.create(identifier='G1', size='SMALL', airport=airport)
        Gate.objects.create(identifier='G2', size='SMALL', airport=airport)
        response = c.post(f'/atc/gates/{gate1.id}/update/', {'identifier': 'G2', 'size': 'SMALL', 'airport': airport.id})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # gate with invalid size
        response = c.post(f'/atc/gates/{gate1.id}/update/', {'identifier': 'G1', 'size': 'TANGO', 'airport': airport.id})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # cleanup
        Gate.objects.all().delete()
        Airport.objects.all().delete()

    def test_gate_delete_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # delete non existent gate
        response = c.post(f'/atc/gates/1/delete/')
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

class RunwayTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='temporary', email='temporary@gmail.com',
                                                  password='temporary')

    def test_runway_create_edit_delete(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # dependencies: Airport
        response = c.post('/atc/airports/create/', {'name': 'Runway Test Airport', 'x': '0.0', 'y': '0.0'})
        self.assertLess(response.status_code, 400)
        airport = Airport.objects.get(name='Runway Test Airport')

        response = c.post('/atc/runways/create/', {'identifier': 'R1', 'size': 'SMALL', 'airport': airport.id})
        self.assertLess(response.status_code, 400)
        runway = Runway.objects.get(identifier='R1')
        self.assertIsNotNone(runway)
        self.assertEqual(runway.size, 'SMALL')
        self.assertEqual(runway.airport, airport)

        response = c.post(f'/atc/runways/{runway.id}/update/', {'identifier': 'R1', 'size': 'MEDIUM', 'airport': airport.id})
        self.assertLess(response.status_code, 400)
        runway = Runway.objects.get(identifier='R1')
        self.assertIsNotNone(runway)
        self.assertEqual(runway.size, 'MEDIUM')
        self.assertEqual(runway.airport, airport)

        response = c.post(f'/atc/runways/{runway.id}/delete/')
        self.assertLess(response.status_code, 400)
        try:
            runway = Runway.objects.get(identifier='R1')
            self.assertTrue(True, False) # we should not have gotten here
        except Runway.DoesNotExist:
            pass

        # cleanup
        Runway.objects.all().delete()
        Runway.objects.all().delete()

    def test_runway_create_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # runway with same name creation
        airport = Airport.objects.create(name='Runway Test Airport', x=0.0, y=0.0)
        Runway.objects.create(identifier='R1', size='SMALL', airport=airport)
        response = c.post('/atc/runways/create/', {'identifier': 'R1', 'size': 'SMALL', 'airport': airport.id})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)
        # gate with invalid size
        response = c.post('/atc/runways/create/', {'identifier': 'R2', 'size': 'TANGO', 'airport': airport.id})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # cleanup
        Runway.objects.all().delete()
        Airport.objects.all().delete()

    def test_runway_update_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # runway with same name during update
        airport = Airport.objects.create(name='Runway Test Airport', x=0.0, y=0.0)
        runway1 = Runway.objects.create(identifier='R1', size='SMALL', airport=airport)
        Runway.objects.create(identifier='R2', size='SMALL', airport=airport)
        response = c.post(f'/atc/runways/{runway1.id}/update/', {'identifier': 'R2', 'size': 'SMALL', 'airport': airport.id})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # gate with invalid size
        response = c.post(f'/atc/runways/{runway1.id}/update/', {'identifier': 'R1', 'size': 'TANGO', 'airport': airport.id})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # cleanup
        Runway.objects.all().delete()
        Airport.objects.all().delete()

    def test_runway_delete_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # delete non existent runway
        response = c.post(f'/atc/runways/1/delete/')
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

class PlaneTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='temporary', email='temporary@gmail.com',
                                                  password='temporary')

    def test_plane_create_edit_delete(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # dependencies: Airline, Gate, Runway
        airport = Airport.objects.create(name='Runway Test Airport', x=0.0, y=0.0)
        response = c.post('/atc/airlines/create/', {'name': 'Plane Test Airline', 'airports': [airport.id]})
        self.assertLess(response.status_code, 400)
        airline = Airline.objects.get(name='Plane Test Airline')
        response = c.post('/atc/gates/create/', {'identifier': 'G1', 'size': 'SMALL', 'airport': airport.id})
        self.assertLess(response.status_code, 400)
        gate = Gate.objects.get(identifier='G1')
        response = c.post('/atc/runways/create/', {'identifier': 'R1', 'size': 'SMALL', 'airport': airport.id})
        self.assertLess(response.status_code, 400)
        runway = Runway.objects.get(identifier='R1')

        response = c.post('/atc/planes/create/', {'identifier': 'P1', 'size': 'SMALL', 'currentPassengerCount': 20, 'maxPassengerCount': 250, 'airline': airline.id, 'gate': gate.id, 'runway': runway.id})
        self.assertLess(response.status_code, 400)
        plane = Plane.objects.get(identifier='P1')
        self.assertIsNotNone(plane)
        self.assertEqual(plane.size, 'SMALL')
        self.assertEqual(plane.currentPassengerCount, 20)
        self.assertEqual(plane.maxPassengerCount, 250)
        self.assertEqual(plane.airline, airline)
        self.assertEqual(plane.gate, gate)
        self.assertEqual(plane.runway, runway)

        response = c.post(f'/atc/planes/{plane.id}/update/', {'identifier': 'P2', 'size': 'SMALL', 'currentPassengerCount': 20, 'maxPassengerCount': 250, 'airline': airline.id, 'gate': gate.id, 'runway': runway.id})
        self.assertLess(response.status_code, 400)
        plane = Plane.objects.get(identifier='P2')
        self.assertIsNotNone(plane)
        self.assertEqual(plane.size, 'SMALL')
        self.assertEqual(plane.currentPassengerCount, 20)
        self.assertEqual(plane.maxPassengerCount, 250)
        self.assertEqual(plane.airline, airline)
        self.assertEqual(plane.gate, gate)
        self.assertEqual(plane.runway, runway)

        response = c.post(f'/atc/planes/{plane.id}/delete/')
        self.assertLess(response.status_code, 400)
        try:
            plane = Plane.objects.get(identifier='P1')
            self.assertTrue(True, False) # we should not have gotten here
        except Plane.DoesNotExist:
            pass

        # cleanup
        Gate.objects.all().delete()
        Runway.objects.all().delete()
        Airline.objects.all().delete()
        Plane.objects.all().delete()
        Airport.objects.all().delete()

    def test_plane_create_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # runway with same name creation
        airline = Airline.objects.create(name='Plane Test Airline')
        Plane.objects.create(identifier='P1', size='SMALL', currentPassengerCount=20, maxPassengerCount=250, airline=airline)
        response = c.post('/atc/planes/create/', {'identifier': 'P1', 'size': 'SMALL', 'currentPassengerCount': 20, 'maxPassengerCount': 250, 'airline': airline.id})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)
        # gate with invalid size
        response = c.post('/atc/planes/create/', {'identifier': 'P2', 'size': 'TANGO', 'currentPassengerCount': 20, 'maxPassengerCount': 250, 'airline': airline.id})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # cleanup
        Plane.objects.all().delete()
        Airport.objects.all().delete()

    def test_plane_update_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # plane with same name during update
        airline = Airline.objects.create(name='Plane Test Airline')
        plane1 = Plane.objects.create(identifier='P1', size='SMALL', currentPassengerCount=20, maxPassengerCount=250, airline=airline)
        Plane.objects.create(identifier='P2', size='SMALL', currentPassengerCount=20, maxPassengerCount=250, airline=airline)
        response = c.post(f'/atc/runways/{plane1.id}/update/', {'identifier': 'P2', 'size': 'SMALL', 'currentPassengerCount': 20, 'maxPassengerCount': 250, 'airline': airline.id})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # gate with invalid size
        response = c.post(f'/atc/runways/{plane1.id}/edit/', {'identifier': 'P1', 'size': 'TANGO', 'currentPassengerCount': 20, 'maxPassengerCount': 250, 'airline': airline.id})
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

        # cleanup
        Plane.objects.all().delete()
        Airport.objects.all().delete()

    def test_plane_delete_validation(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        # delete non existent plane
        response = c.post(f'/atc/planes/1/delete/')
        # should fail
        self.assertGreaterEqual(response.status_code, 400)

@patch("atc.helpers.send_imminent_collision_post", autospec=True)
class SimulationTests(TestCase):
    def setUp(self):
        management.call_command("load_data")

    def test_head_on_collision(self, mock_call_external_api):
        c = Client()
        self.assertEqual(mock_call_external_api.called, False)
        plane1 = Plane.objects.filter(identifier="gnfasudtlm").first()
        plane2 = Plane.objects.filter(identifier="matxovlzow").first()
        airport1 = Airport.objects.filter(name="kkz").first()
        airport2 = Airport.objects.filter(name="xhz").first()
        take_off = datetime.now()
        landing = datetime.now() + timedelta(hours=1)

        c.post('/atc/planes/update/', data=json.dumps({
            "plane": plane1.identifier,
            "direction": calc_heading(airport1, airport2),
            "speed": calc_distance(airport1, airport2),
            "origin": airport1.name,
            "destination": airport2.name,
            "take_off_time": take_off.strftime("%Y-%m-%d %H:%M"),
            "landing_time": landing.strftime("%Y-%m-%d %H:%M")
        }), content_type="application/json")
        c.post('/atc/planes/update/', data=json.dumps({
            "plane": plane2.identifier,
            "direction": calc_heading(airport2, airport1),
            "speed": calc_distance(airport2, airport1),
            "origin": airport2.name,
            "destination": airport1.name,
            "take_off_time": take_off.strftime("%Y-%m-%d %H:%M"),
            "landing_time": landing.strftime("%Y-%m-%d %H:%M")
        }), content_type="application/json")
        self.assertEqual(mock_call_external_api.called, True)

    def test_rear_collision(self, mock_call_external_api):
        c = Client()
        self.assertEqual(mock_call_external_api.called, False)
        plane1 = Plane.objects.filter(identifier="gnfasudtlm").first()
        plane2 = Plane.objects.filter(identifier="matxovlzow").first()
        airport1 = Airport.objects.filter(name="kkz").first()
        airport2 = Airport.objects.filter(name="xhz").first()
        take_off = datetime.now()
        landing1 = datetime.now() + timedelta(hours=1)

        c.post('/atc/planes/update/', data=json.dumps({
            "plane": plane1.identifier,
            "direction": calc_heading(airport1, airport2),
            "speed": calc_distance(airport1, airport2) / 2.5,
            "origin": airport1.name,
            "destination": airport2.name,
            "take_off_time": (take_off - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M"),
            "landing_time": (landing1 + timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M")
        }), content_type="application/json")
        c.post('/atc/planes/update/', data=json.dumps({
            "plane": plane2.identifier,
            "direction": calc_heading(airport1, airport2),
            "speed": calc_distance(airport1, airport2),
            "origin": airport1.name,
            "destination": airport2.name,
            "take_off_time": take_off.strftime("%Y-%m-%d %H:%M"),
            "landing_time": landing1.strftime("%Y-%m-%d %H:%M")
        }), content_type="application/json")
        self.assertEqual(mock_call_external_api.called, True)

    def test_tbone_collision(self, mock_call_external_api):
        c = Client()
        self.assertEqual(mock_call_external_api.called, False)
        plane1 = Plane.objects.filter(identifier="gnfasudtlm").first()
        plane2 = Plane.objects.filter(identifier="matxovlzow").first()
        airport1 = Airport.objects.filter(name="oap").first()
        airport2 = Airport.objects.filter(name="kkz").first()
        airport3 = Airport.objects.filter(name="mfz").first()
        take_off = datetime.now()
        landing = datetime.now() + timedelta(hours=1)

        c.post('/atc/planes/update/', data=json.dumps({
            "plane": plane1.identifier,
            "direction": calc_heading(airport1, airport3),
            "speed": calc_distance(airport1, airport3),
            "origin": airport1.name,
            "destination": airport3.name,
            "take_off_time": take_off.strftime("%Y-%m-%d %H:%M"),
            "landing_time": landing.strftime("%Y-%m-%d %H:%M")
        }), content_type="application/json")
        c.post('/atc/planes/update/', data=json.dumps({
            "plane": plane2.identifier,
            "direction": calc_heading(airport2, airport3),
            "speed": calc_distance(airport2, airport3),
            "origin": airport2.name,
            "destination": airport3.name,
            "take_off_time": take_off.strftime("%Y-%m-%d %H:%M"),
            "landing_time": landing.strftime("%Y-%m-%d %H:%M")
        }), content_type="application/json")
        self.assertEqual(mock_call_external_api.called, True)

    def test_duplicate_gate(self, mock_call_external_api):
        c = Client()
        self.assertEqual(mock_call_external_api.called, False)
        plane1 = Plane.objects.filter(identifier="mopyahgbal").first()
        plane2 = Plane.objects.filter(identifier="rzmwdhqblw").first()
        gate = Gate.objects.filter(identifier="jemhnkkldw").first()
        arrival = datetime.now() + timedelta(hours=1)

        c.post('/atc/gates/assignment/', data=json.dumps({
            "plane": plane1.identifier,
            "gate": gate.identifier,
            "arrive_at_time": arrival.strftime("%Y-%m-%d %H:%M")
        }), content_type="application/json")
        c.post('/atc/gates/assignment/', data=json.dumps({
            "plane": plane2.identifier,
            "gate": gate.identifier,
            "arrive_at_time": arrival.strftime("%Y-%m-%d %H:%M")
        }), content_type="application/json")
        self.assertEqual(mock_call_external_api.called, True)

    def test_duplicate_runway(self, mock_call_external_api):
        c = Client()
        self.assertEqual(mock_call_external_api.called, False)
        plane1 = Plane.objects.filter(identifier="mopyahgbal").first()
        plane2 = Plane.objects.filter(identifier="rzmwdhqblw").first()
        runway = Runway.objects.filter(identifier="qkegovbsbo").first()
        arrival = datetime.now() + timedelta(hours=1)

        c.post('/atc/runways/assignment/', data=json.dumps({
            "plane": plane1.identifier,
            "runway": runway.identifier,
            "arrive_at_time": arrival.strftime("%Y-%m-%d %H:%M")
        }), content_type="application/json")
        c.post('/atc/runways/assignment/', data=json.dumps({
            "plane": plane2.identifier,
            "runway": runway.identifier,
            "arrive_at_time": arrival.strftime("%Y-%m-%d %H:%M")
        }), content_type="application/json")
        self.assertEqual(mock_call_external_api.called, True)





