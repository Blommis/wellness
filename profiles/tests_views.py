from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='kalle', email='kalle@example.com', password='testpass123'
        )
        self.profile = self.user.userprofile

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_profile_view_logged_in(self):
        self.client.login(username='kalle', password='testpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertIn('form', response.context)
        self.assertIn('orders', response.context)

    def test_profile_update_post(self):
        self.client.login(username='kalle', password='testpass123')
        post_data = {
            'default_phone_number': '0701234567',
            'default_street_address1': 'Exempelgatan 1',
            'default_street_address2': '',
            'default_postcode': '12345',
            'default_town_or_city': 'Karlstad',
            'default_county': 'Värmland',
            'default_country': 'SE',
        }
        response = self.client.post(reverse('profile'), post_data)
        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_town_or_city, 'Karlstad')
