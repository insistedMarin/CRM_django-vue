from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from ..models import Customer, SalesOpportunity
from ..serializers import SalesOpportunitySerializer

class SalesOpportunityTests(APITestCase):
    
    def setUp(self):
        # 创建一个测试用户
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.access_token = str(AccessToken.for_user(self.user))
        self.api_authentication()
        
        # 创建一个客户
        self.customer = Customer.objects.create(
            name='John Doe',
            company='Example Corp',
            email='john@example.com'
        )

        # 创建一个销售机会
        self.sales_opportunity = SalesOpportunity.objects.create(
            customer=self.customer,
            expected_revenue=1000.0,
            current_stage='initial_contact'
        )

        self.valid_payload = {
            'customer': self.customer.id,
            'expected_revenue': 1500.0,
            'current_stage': 'proposal'
        }

        self.invalid_payload = {
            'customer': self.customer.id,
            'expected_revenue': -100.0,  # 无效的预期收入
            'current_stage': 'invalid_stage'  # 无效的销售机会阶段
        }

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

    def test_create_valid_sales_opportunity(self):
        url = reverse('salesopportunity-list')
        response = self.client.post(url, self.valid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SalesOpportunity.objects.count(), 2)

    def test_create_invalid_sales_opportunity(self):
        url = reverse('salesopportunity-list')
        response = self.client.post(url, self.invalid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(SalesOpportunity.objects.count(), 1)

    def test_get_sales_opportunities(self):
        url = reverse('salesopportunity-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_sales_opportunity(self):
        url = reverse('salesopportunity-detail', args=[self.sales_opportunity.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['expected_revenue'], '1000.00')

    def test_update_sales_opportunity(self):
        url = reverse('salesopportunity-detail', args=[self.sales_opportunity.id])
        response = self.client.put(url, self.valid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(SalesOpportunity.objects.get(id=self.sales_opportunity.id).expected_revenue), '1500.00')

    def test_delete_sales_opportunity(self):
        url = reverse('salesopportunity-detail', args=[self.sales_opportunity.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SalesOpportunity.objects.count(), 0)
