from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Plane
import datetime

NOW = datetime.datetime.now()

class CRUD_plane_IntegrationTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='temporary',
            email='temporary@gmail.com',
            password='temporary')

    def test_create_edit_delete(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)

        # TEST - Create
        response = c.post('/plane/create',
                          {'name': 'test_item', 
                           'airline': 'airline'
                           'size': 'large', 
                           'max_occupancy': 500, 
                           'cur_occupancy': 0, 
                           'speed': 10, 
                           'x': 0, 
                           'y': 0, 
                           'heading': 0, 
                           'dt_arrival': NOW
                          })
        self.assertLess(response.status_code, 400)
        test_item = Plane.objects.get(name='test_item')
        self.assertIsNotNone(test_item)
        self.assertEqual(test_item.name, 'test_item')
        self.assertEqual(test_item.airline, 'airline')
        self.assertEqual(test_item.size, 'large')
        self.assertEqual(test_item.max_occupancy, 500)
        self.assertEqual(test_item.cur_occupancy, 0)
        self.assertEqual(test_item.speed, 10)
        self.assertEqual(test_item.x, 0)
        self.assertEqual(test_item.y, 0)
        self.assertEqual(test_item.heading, 0)
        self.assertEqual(test_item.dt_arrival, NOW)

        # TEST - Update
        response = c.post(
            f'/plane/{test_item.id}/update', 
                          {'name': 'renamed', 
                           'airline': 'renamed'
                           'size': 'small', 
                           'max_occupancy': 50, 
                           'cur_occupancy': 1, 
                           'speed': 1, 
                           'x': 1, 
                           'y': 1, 
                           'heading': 180, 
                           'dt_arrival': NOW + 1
                          })
        self.assertLess(response.status_code, 400)
        test_item = Plane.objects.get(name='renamed')
        self.assertIsNotNone(test_item)
        self.assertEqual(test_item.name, 'renamed')
        self.assertEqual(test_item.airline, 'renamed')
        self.assertEqual(test_item.size, 'small')
        self.assertEqual(test_item.max_occupancy, 50)
        self.assertEqual(test_item.cur_occupancy, 1)
        self.assertEqual(test_item.speed, 1)
        self.assertEqual(test_item.x, 1)
        self.assertEqual(test_item.y, 1)
        self.assertEqual(test_item.heading, 180)
        self.assertEqual(test_item.dt_arrival, NOW + 1)

        # TEST - Delete
        response = c.post(f'/plane/{test_item.id}/delete')
        try:
            todo = Plane.objects.get(name='renamed')
            self.assertTrue(True, False)  # we should not have gotten here
        except Todo.DoesNotExist:
            pass

        # cleanup
        Plane.objects.all().delete()
