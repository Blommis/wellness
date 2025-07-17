from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from products.models import Supplement


class CheckoutViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.supplement = Supplement.objects.create(
            name="Test Supplement",
            description="Description",
            price=Decimal('19.99'),
            sku="TEST123"
        )
        self.bag_key = f"supplement_{self.supplement.id}"
        session = self.client.session
        session['bag'] = {
            self.bag_key: {'type': 'supplement', 'quantity': 1}
        }
        session.save()

    def test_checkout_view_get(self):
        """Test GET request renders checkout page"""
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_view_empty_bag_redirect(self):
        """Test redirection if bag is empty"""
        session = self.client.session
        session['bag'] = {}
        session.save()
        response = self.client.get(reverse('checkout'))
        self.assertRedirects(response, reverse('home'))

    def test_checkout_success_redirects_with_invalid_pid(self):
        """Test redirect when order not found by stripe_pid"""
        response = self.client.get(
            reverse('checkout_success', args=['fake_pid'])
        )
        self.assertRedirects(response, reverse('home'))

    def test_checkout_post_valid_data_redirects(self):
        """Test valid form POST triggers redirect"""
        form_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'country': 'SE',
            'postcode': '12345',
            'town_or_city': 'Stockholm',
            'street_address1': 'Street 1',
            'street_address2': '',
            'county': 'Stockholm',
            'client_secret': 'test_secret_abc123'
        }
        response = self.client.post(reverse('checkout'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse('checkout_success', args=['test'])
        )

    def test_checkout_post_invalid_data_shows_error(self):
        """Test invalid form POST (missing fields) shows error"""
        form_data = {
            'full_name': '',
            'email': '',
            'phone_number': '',
            'country': '',
            'postcode': '',
            'town_or_city': '',
            'street_address1': '',
            'street_address2': '',
            'county': '',
            'client_secret': 'test_secret_invalid'
        }
        response = self.client.post(reverse('checkout'), form_data)
        self.assertRedirects(response, reverse('checkout'))
