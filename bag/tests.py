from django.test import TestCase, Client
from django.urls import reverse, resolve
from decimal import Decimal
from products.models import Supplement, MealPlan
from bag import views as bag_views
# Create your tests here.

"""Testing for views.py and urls.py"""


class BagViewTests(TestCase):
    """Tests for the shopping bag views"""

    def setUp(self):
        """Create sample products and test client"""
        self.client = Client()
        self.supplement = Supplement.objects.create(
            name="Whey Protein",
            description="Test description",
            price=Decimal('10.00'),
            sku="WHEY-001"
        )
        self.mealplan = MealPlan.objects.create(
            name="Keto Plan",
            description="Low-carb plan",
            calories=1500,
            price=Decimal('20.00')
        )

    def test_view_bag_empty(self):
        """Test view bag page with empty cart"""
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_supplement_to_bag(self):
        """Test adding a supplement to the cart"""

        self.client.post(reverse('add_to_bag'), {
            'product_id': self.supplement.id,
            'product_type': 'supplement',
            'quantity': 2,
            'redirect_url': reverse('view_bag')
        })
        bag = self.client.session['bag']
        key = f'supplement_{self.supplement.id}'
        self.assertIn(key, bag)
        self.assertEqual(bag[key]['quantity'], 2)

    def test_add_mealplan_to_bag(self):
        """Test adding a meal plan to the cart"""

        self.client.post(reverse('add_to_bag'), {
            'product_id': self.mealplan.id,
            'product_type': 'mealplan',
            'quantity': 3,
            'redirect_url': reverse('view_bag')
        })
        bag = self.client.session['bag']
        key = f'mealplan_{self.mealplan.id}'
        self.assertIn(key, bag)
        self.assertEqual(bag[key]['quantity'], 1)  # should always be 1

    def test_remove_item_from_bag(self):
        """Test removing item from the cart"""
        session = self.client.session
        session['bag'] = {
            f'supplement_{self.supplement.id}': {'type': 'supplement',
                                                 'quantity': 2}
        }
        session.save()
        item_key = f'supplement_{self.supplement.id}'
        response = self.client.get(reverse('remove_from_bag', args=[item_key]))
        self.assertRedirects(response, reverse('view_bag'))
        self.assertNotIn(item_key, self.client.session.get('bag', {}))


class BagURLTests(TestCase):
    """Tests for URL-to-view resolution"""

    def test_view_bag_url_resolves(self):
        self.assertEqual(resolve(reverse('view_bag')).func, bag_views.view_bag)

    def test_add_to_bag_url_resolves(self):
        self.assertEqual(resolve(reverse('add_to_bag')).func,
                         bag_views.add_to_bag)

    def test_remove_from_bag_url_resolves(self):
        url = reverse('remove_from_bag', args=['supplement_1'])
        self.assertEqual(resolve(url).func, bag_views.remove_from_bag)
