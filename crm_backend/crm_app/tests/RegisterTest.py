from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class RegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')

    def test_user_registration_with_correct_verification_code(self):
        email = "testuser456@example.com"
        verification_code = "123456"
        cache.set(email, verification_code, 600)

        data = {
            "username": "testuser456",
            "password": "Testpassword123!",
            "password_confirm": "Testpassword123!",
            "email": email,
            "verification_code": verification_code
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_registration_with_wrong_verification_code(self):
        data = {
            "username": "testuser456",
            "password": "Testpassword123!",
            "password_confirm": "Testpassword123!",
            "email": "testuser456@example.com",
            "verification_code": "654321"
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_username_registration(self):
        # create user
        User.objects.create_user(
            username='existinguser',
            password='TestPassword123!',
            email='existinguser@example.com',
        )

        data = {
            'username': 'existinguser',  # duplicate username
            'password': 'TestPassword123!',
            'email': 'testuser@example.com',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
