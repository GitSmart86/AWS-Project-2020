from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import Airport


class CRUD_airport_IntegrationTestCases(TestCase):
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
        response = c.post('/airport/create',
                          {'name': 'test_item', 'x': 0, 'y': 0})
        self.assertLess(response.status_code, 400)
        test_item = Airport.objects.get(name='test_item')
        self.assertIsNotNone(test_item)
        self.assertEqual(test_item.name, 'test_item')
        self.assertEqual(test_item.y, 0)
        self.assertEqual(test_item.x, 0)

        # TEST - Update
        response = c.post(
            f'/airport/{test_item.id}/update', {'name': 'renamed', 'x': 1, 'y': 1})
        self.assertLess(response.status_code, 400)
        test_item = Airport.objects.get(name='renamed')
        self.assertEqual(test_item.name, 'rename')
        self.assertEqual(test_item.y, 1)
        self.assertEqual(test_item.x, 1)

        # TEST - Delete
        response = c.post(f'/airport/{test_item.id}/delete')
        try:
            todo = Airport.objects.get(name='renamed')
            self.assertTrue(True, False)  # we should not have gotten here
        except Todo.DoesNotExist:
            pass

        # cleanup
        Airport.objects.all().delete()
