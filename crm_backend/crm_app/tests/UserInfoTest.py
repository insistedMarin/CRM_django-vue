from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken


class GetUserInfoTests(APITestCase):
    def setUp(self):
        # 创建测试用户
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.access_token = str(AccessToken.for_user(self.user))
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

    def test_get_user_info_authenticated(self):
        response = self.client.get("/user_info/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_get_user_info_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/user_info/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
