from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from products.models import Supplement, MealPlan
from recipes.models import Breakfast, Lunch, Snack


class ProductViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.supplement = Supplement.objects.create(
            name="Vitamin C",
            description="Boosts immunity",
            price=Decimal("9.99"), sku="VC100"
        )
        self.mealplan = MealPlan.objects.create(
            name="Keto Plan",
            description="Low carb",
            calories=1500,
            price=Decimal("29.99"),
            sku="KETO001"
        )
        self.breakfast = Breakfast.objects.create(
            name="Oatmeal", short_description="Oats",
            description="Warm and filling"
        )
        self.lunch = Lunch.objects.create(
            name="Chicken Salad",
            short_description="Healthy",
            description="With avocado"
        )
        self.snack = Snack.objects.create(
            name="Protein Bar",
            short_description="Snack",
            description="Post workout bar"
        )

    def test_supplements_view(self):
        response = self.client.get(reverse("products:supplements"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/supplements.html")

    def test_supplement_detail_view(self):
        response = self.client.get(
            reverse("products:supplement_detail", args=[self.supplement.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/supplement_detail.html")

    def test_mealplan_view(self):
        response = self.client.get(reverse("products:view_mealplan"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/mealplan.html")

    def test_search_redirect_keywords(self):
        self.assertRedirects(self.client.get(
            reverse("products:search_results"), {"q": "supplement"}),
            reverse("products:supplements")
        )
        self.assertRedirects(self.client.get(
            reverse("products:search_results"), {"q": "mealplans"}),
            reverse("products:view_mealplan")
        )
        self.assertRedirects(self.client.get(
            reverse("products:search_results"), {"q": "recipes"}),
            reverse("recipes:recipes")
        )

    def test_search_with_matches(self):
        response = self.client.get(
            reverse("products:search_results"), {"q": "Vitamin"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Vitamin C")

    def test_search_without_query(self):
        response = self.client.get(reverse("products:search_results"))
        self.assertRedirects(response, reverse("home"))
