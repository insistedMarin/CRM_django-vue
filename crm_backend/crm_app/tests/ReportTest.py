from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from ..models import Report

class ReportTests(APITestCase):
    
    def setUp(self):
        # 创建一个测试用户
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.access_token = str(AccessToken.for_user(self.user))
        self.api_authentication()
        
        # 创建一个报告
        self.report = Report.objects.create(
            report_type='sales_funnel',
            data='{"data": "Sales Funnel Data"}'
        )

        self.valid_payload = {
            'report_type': 'monthly_sales',
            'data': '{"data": "Monthly Sales Data"}'
        }

        self.invalid_payload = {
            'report_type': 'invalid_report_type',  # 无效的报告类型
            'data': 'Invalid Data'  # 无效的数据格式
        }

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

    def test_create_valid_report(self):
        url = reverse('report-list')
        response = self.client.post(url, self.valid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Report.objects.count(), 2)

    def test_create_invalid_report(self):
        url = reverse('report-list')
        response = self.client.post(url, self.invalid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Report.objects.count(), 1)

    def test_get_reports(self):
        url = reverse('report-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_report(self):
        url = reverse('report-detail', args=[self.report.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['report_type'], 'sales_funnel')

    def test_update_report(self):
        url = reverse('report-detail', args=[self.report.id])
        response = self.client.put(url, self.valid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Report.objects.get(id=self.report.id).report_type, 'monthly_sales')

    def test_delete_report(self):
        url = reverse('report-detail', args=[self.report.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Report.objects.count(), 0)
