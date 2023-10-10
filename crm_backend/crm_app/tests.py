from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class RegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')

    def test_user_registration(self):
        data = {
            "username": "testuser456",
            "password": "Testpassword123!",
            "password_confirm": "Testpassword123!",
            "email": "testuser456@example.com"
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

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


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('login')

    def test_user_login(self):
        # 创建一个用户
        User.objects.create_user(
            username='testuser',
            password='TestPassword123!',
            email='testuser@example.com',
        )

        data = {
            'username': 'testuser',
            'password': 'TestPassword123!',
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_credentials_login(self):
        data = {
            'username': 'nonexistentuser',  # not exist username
            'password': 'InvalidPassword123!',
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
