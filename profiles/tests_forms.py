from django.test import TestCase
from profiles.forms import UserProfileForm


class UserProfileFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'default_phone_number': '0701234567',
            'default_street_address1': 'Main Street 1',
            'default_street_address2': '',
            'default_postcode': '12345',
            'default_town_or_city': 'Stockholm',
            'default_county': 'Stockholms län',
            'default_country': 'SE',
        }

    def test_user_profile_form_valid(self):
        form = UserProfileForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_user_profile_form_missing_required_fields(self):
        # Remove a required field
        data = self.valid_data.copy()
        data.pop('default_phone_number')
        form = UserProfileForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('default_phone_number', form.errors)

    def test_user_profile_form_optional_address2(self):
        data = self.valid_data.copy()
        data['default_street_address2'] = ''
        form = UserProfileForm(data=data)
        self.assertTrue(form.is_valid())
