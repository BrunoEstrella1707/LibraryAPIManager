from django.test import TestCase
from users.models import CustomUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class CustomUserTests(APITestCase):
    def test_creat_account(self):

        url = reverse('user-list')
        data = {
            "email": "testador@email.com",
            "username": "testador",
            "name": "Programador",
            "password": "t3st_p4ss!",
            "confirm_password": "t3st_p4ss!",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().name, 'Programador')
        self.assertEqual(CustomUser.objects.get().username, 'testador')