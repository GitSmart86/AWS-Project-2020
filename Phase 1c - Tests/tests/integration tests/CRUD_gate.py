from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Gate
import datetime

NOW = datetime.datetime.now()

class CRUD_gate_IntegrationTestCases(TestCase):
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
        response = c.post('/gate/create',
                          {'name': 'test_item',
                           'size': 'medium',
                           'dt_available': NOW
                           })
        self.assertLess(response.status_code, 400)
        test_item = Gate.objects.get(name='test_item')
        self.assertEqual(test_item.name, 'test_item'))
        self.assertEqual(test_item.size, 'medium'))
        self.assertEqual(test_item.dt_available, NOW)
        self.assertIsNotNone(test_item)

        # TEST - Update
        response = c.post(
            f'/gate/{test_item.id}/update', 
                          {'name': 'renamed',
                           'size': 'small',
                           'dt_available': NOW + 1
                           })
        self.assertLess(response.status_code, 400)
        test_item = Gate.objects.get(name='renamed')
        self.assertEqual(test_item.name, 'renamed'))
        self.assertEqual(test_item.size, 'small'))
        self.assertEqual(test_item.dt_available, NOW + 1)

        # TEST - Delete
        response = c.post(f'/gate/{test_item.id}/delete')
        try:
            todo = Gate.objects.get(name='renamed')
            self.assertTrue(True, False)  # we should not have gotten here
        except Todo.DoesNotExist:
            pass

        # cleanup
        Gate.objects.all().delete()
