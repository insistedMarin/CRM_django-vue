    from rest_framework.test import APITestCase
    from rest_framework import status
    from django.urls import reverse
    from django.contrib.auth.models import User
    from rest_framework_simplejwt.tokens import AccessToken
    from ..models import Customer


    class CustomerTests(APITestCase):

        def setUp(self):
            self.user = User.objects.create_user(username='testuser', password='testpassword')
            self.access_token = str(AccessToken.for_user(self.user))
            self.api_authentication()
            self.customer = Customer.objects.create(
                name='John Doe',
                company='Example Corp',
                job_title='Engineer',
                phone='1234567890',
                email='john@example.com',
                address='123 Main St, Springfield',
                interactions='Met at a conference.'
            )

            self.valid_payload = {
                'name': 'Jane Smith',
                'company': 'Tech Inc',
                'job_title': 'Developer',
                'phone': '0987654321',
                'email': 'jane@example.com',
                'address': '456 Elm St, Springfield',
                'interactions': 'Introduced via email.'
            }

            self.invalid_payload = {
                'name': '',
                'company': '',
                'email': 'jane@example.com',
                'phone': '0987654321',
                # 其他字段...
            }

        def api_authentication(self):
            self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

        def test_create_valid_customer(self):
            url = reverse('customer-list')
            response = self.client.post(url, self.valid_payload, format='json')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Customer.objects.count(), 2)

        def test_create_invalid_customer(self):
            url = reverse('customer-list')
            response = self.client.post(url, self.invalid_payload, format='json')

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(Customer.objects.count(), 1)

        def test_get_customers(self):
            url = reverse('customer-list')
            response = self.client.get(url)

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 1)

        def test_get_single_customer(self):
            url = reverse('customer-detail', args=[self.customer.id])
            response = self.client.get(url)

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['name'], self.customer.name)

        def test_update_customer(self):
            url = reverse('customer-detail', args=[self.customer.id])
            response = self.client.put(url, self.valid_payload, format='json')

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(Customer.objects.get(id=self.customer.id).name, 'Jane Smith')

        def test_delete_customer(self):
            url = reverse('customer-detail', args=[self.customer.id])
            response = self.client.delete(url)

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(Customer.objects.count(), 0)
