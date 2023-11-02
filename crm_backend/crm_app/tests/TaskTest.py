from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from ..models import Task, Customer  # 导入 Customer 模型

class TaskTests(APITestCase):
    
    def setUp(self):
        # 创建一个测试用户
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.access_token = str(AccessToken.for_user(self.user))
        self.api_authentication()
        
        # 创建一个客户
        self.customer = Customer.objects.create(
            name='Test Customer',
            company='Test Company',
            email='test@example.com'
        )
        
        # 创建一个任务
        self.task = Task.objects.create(
            user=self.user,
            customer=self.customer,  # 设置任务的客户
            title='Sample Task',
            description='Task description',
            due_date='2023-11-15T12:00:00Z'
        )

        # 创建一个有效的任务数据
        self.valid_payload = {
            'user': self.user.id,
            'customer': self.customer.id,
            'title': 'New Task',
            'description': 'New Task description',
            'due_date': '2023-12-01T09:00:00Z'
        }

        # 创建一个无效的任务数据
        self.invalid_payload = {
            'user': self.user.id,
            'customer' :self.customer.id,
            'title': '',  # 无效的标题
            'description': 'Task description',
            'due_date': '2023-11-15T12:00:00Z'
        }

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

    def test_create_valid_task(self):
        url = reverse('task-list')
        response = self.client.post(url, self.valid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_create_invalid_task(self):
        url = reverse('task-list')
        response = self.client.post(url, self.invalid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 1)

    def test_get_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Sample Task')

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.put(url, self.valid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=self.task.id).title, 'New Task')

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

