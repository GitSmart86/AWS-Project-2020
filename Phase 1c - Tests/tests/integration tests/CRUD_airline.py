from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Airline


class CRUD_airline_IntegrationTestCases(TestCase):
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
        response = c.post('/airline/create',
                          {'name': 'test_item'})
        self.assertLess(response.status_code, 400)
        test_item = Airline.objects.get(name='test_item')
        self.assertIsNotNone(test_item)
        self.assertEqual(test_item.name, 'test_item')

        # TEST - Update
        response = c.post(
            f'/airline/{test_item.id}/update', {'name': 'renamed'})
        self.assertLess(response.status_code, 400)
        test_item = Airline.objects.get(name='renamed')
        self.assertEqual(test_item.name, 'rename')

        # TEST - Delete
        response = c.post(f'/airline/{test_item.id}/delete')
        try:
            todo = Airline.objects.get(name='renamed')
            self.assertTrue(True, False)  # we should not have gotten here
        except Todo.DoesNotExist:
            pass

        # cleanup
        Airline.objects.all().delete()
