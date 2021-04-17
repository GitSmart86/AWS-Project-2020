from django.test import Client, TestCase
from django.contrib.auth.models import User
from classes.models import User


class CRUD_user_IntegrationTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='temporary',
            email='temporary@gmail.com',
            password='temporary')

    def test_create_edit_delete(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)

        # TODO - Phase 1d

        # TEST - Create Role

        # TEST - Update Role

        # TEST - Delete Role



        # TEST - Create User
        response = c.post('/user/create',
                          {'username'='test',
                           'email'='test@mail.com',
                           'password'='test'})
        self.assertLess(response.status_code, 400)
        test_item = User.objects.get(name='test')
        self.assertIsNotNone(test_item)
        self.assertEqual(test_item.name, 'test')
        self.assertEqual(test_item.email, 'test@mail.com')
        self.assertEqual(test_item.password, 'test')

        # TEST - Update User
        response = c.post(f'/user/{test_item.id}/update',
                          {'username'='renamed',
                           'email'='renamed@mail.com',
                           'password'='renamed'})
        self.assertLess(response.status_code, 400)
        test_item = User.objects.get(name='renamed')
        self.assertIsNotNone(test_item)
        self.assertEqual(test_item.name, 'renamed')
        self.assertEqual(test_item.email, 'renamed@mail.com')
        self.assertEqual(test_item.password, 'renamed')

        # TEST - Delete User
        response = c.post(f'/user/{test_item.id}/delete')
        try:
            todo = User.objects.get(name='renamed')
            self.assertTrue(True, False)  # we should not have gotten here
        except Todo.DoesNotExist:
            pass

        # cleanup
        User.objects.all().delete()
