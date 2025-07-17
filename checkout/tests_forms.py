from django.test import TestCase
from checkout.forms import OrderForm


class OrderFormTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'full_name': 'Karl Blomquist',
            'email': 'karl@example.com',
            'phone_number': '0701234567',
            'street_address1': 'Storgatan 1',
            'street_address2': '',
            'town_or_city': 'Karlstad',
            'postcode': '12345',
            'county': 'Värmland',
            'country': 'SE',
        }

    def test_order_form_valid_data(self):
        """Form should be valid with proper data"""
        form = OrderForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_order_form_missing_required_field(self):
        """Form should be invalid if a required field is missing"""
        data = self.valid_data.copy()
        data['full_name'] = ''
        form = OrderForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors)

    def test_order_form_fields(self):
        """Form should include all specified fields"""
        form = OrderForm()
        expected_fields = [
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'county', 'country'
        ]
        self.assertEqual(list(form.fields.keys()), expected_fields)
