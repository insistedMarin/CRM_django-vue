
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User


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
