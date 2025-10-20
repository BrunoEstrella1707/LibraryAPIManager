from django.test import TestCase
from users.models import CustomUser
from .models import Author
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class AuthorTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testador',
            email='testador@email.com',
            password='4dm1n_p4ss'
        )
        url = reverse('token_obtain_pair')
        data = {"email": "testador@email.com", "password": "4dm1n_p4ss"}
        response = self.client.post(url, data, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
    

    def test_create_author(self):
        url = reverse('author-list-create')
        data = {"name": "Autor",
                "nationality": "BRA"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get().name, 'Autor')