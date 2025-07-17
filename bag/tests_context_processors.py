from django.test import RequestFactory, TestCase
from decimal import Decimal
from products.models import Supplement, MealPlan
from bag.context_processors import cart_items_count, bag_contents


class ContextProcessorTests(TestCase):
    def setUp(self):
        """
        Set up test data for supplements and meal plans.
        Called before each test method.
        """
        self.factory = RequestFactory()
        self.supplement = Supplement.objects.create(
            name="Whey protein",
            description="High quality protein supplement",
            price=Decimal('10.00'),
            sku="WHEY-001"
        )
        self.mealplan = MealPlan.objects.create(
            name="Keto Plan",
            description="A low-carb, high-fat meal plan",
            calories=1500,
            price=Decimal('20.00'))

    def test_cart_items_count(self):
        """
        Test that cart_items_count returns correct
        total quantity of items in the bag.
        """
        request = self.factory.get('/')
        request.session = {
            'bag': {
                f'supplement_{self.supplement.id}': {'quantity': 2},
                f'mealplan_{self.mealplan.id}': {'quantity': 1}
            }
        }
        context = cart_items_count(request)
        self.assertEqual(context['cart_items'], 3)

    def test_bag_contents(self):
        """Test that bag_contents returns correct values"""
        request = self.factory.get('/')
        request.session = {
            'bag': {
                f'supplement_{self.supplement.id}': {'quantity': 2},
                f'mealplan_{self.mealplan.id}': {'quantity': 1}
            }
        }
        context = bag_contents(request)
        self.assertEqual(len(context['bag_items']), 2)
        self.assertEqual(context['total'], Decimal('40.00'))  # 2*10 + 1*20
        self.assertEqual(context['delivery'], Decimal('7.90'))
        self.assertEqual(context['grand_total'], Decimal('47.90'))
        self.assertEqual(context['product_count'], 3)
