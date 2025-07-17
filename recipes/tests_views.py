from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Breakfast, Lunch, Snack
from reviews.models import Review
from django.contrib.contenttypes.models import ContentType


class RecipeViewsTest(TestCase):
    """ Creates test user and test data for recipes"""
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass"
        )

        self.breakfast = Breakfast.objects.create(
            name="Test Breakfast",
            short_description="Short desc",
            description="Full desc"
        )
        self.lunch = Lunch.objects.create(
            name="Test Lunch",
            short_description="Short desc",
            description="Full desc"
        )
        self.snack = Snack.objects.create(
            name="Test Snack",
            short_description="Short desc",
            description="Full desc"
        )

    def test_recipes_view(self):
        """ testing to see if page loads correctly """
        response = self.client.get(reverse("recipes:recipes"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipes.html")

    def test_recipe_detail_view(self):
        """ testing to see if recipe detail shows right breakfast recipe"""
        response = self.client.get(
            reverse("recipes:recipe_detail",
                    args=["breakfast", self.breakfast.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipe_detail.html")
        self.assertContains(response, self.breakfast.name)

    def test_post_review_authenticated(self):
        """ testing if logged in user can post a review"""
        self.client.login(username="testuser", password="testpass")
        url = reverse(
            "recipes:recipe_detail", args=["breakfast", self.breakfast.pk]
        )
        response = self.client.post(url, {
            "rating": 5,
            "comment": "Great breakfast!"
        })
        self.assertEqual(response.status_code, 302)

        content_type = ContentType.objects.get_for_model(Breakfast)
        review_exists = Review.objects.filter(
            user=self.user,
            content_type=content_type,
            object_id=self.breakfast.pk
        ).exists()
        self.assertTrue(review_exists)

    def test_delete_review(self):
        """ testing to see if user can delete own review"""

        self.client.login(username="testuser", password="testpass")
        content_type = ContentType.objects.get_for_model(Breakfast)
        review = Review.objects.create(
            user=self.user,
            content_type=content_type,
            object_id=self.breakfast.pk,
            rating=4,
            comment="Tasty!"
        )
        delete_url = reverse("recipes:delete_review", args=[review.pk])
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Review.objects.filter(pk=review.pk).exists())
