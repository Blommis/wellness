from django.test import TestCase
from django.urls import reverse
from .models import GalleryImage
# Create your tests here.


class GalleryImageModelTest(TestCase):
    def test_can_create_gallery_image(self):
        """Test that a GalleryImage instance can be created"""
        image = GalleryImage.objects.create(image='sample_image.jpg')
        self.assertEqual(GalleryImage.objects.count(), 1)
        self.assertEqual(image.image, 'sample_image.jpg')

    def test_str_method_returns_image_field(self):
        """Test that __str__ returns the image field as string"""
        image = GalleryImage.objects.create(image='example.jpg')
        self.assertEqual(str(image), 'example.jpg')


class AboutViewTests(TestCase):
    """Testing if about-views works correctly"""

    def setUp(self):
        """Creates test image in database before every test"""
        GalleryImage.objects.create(
            image="https://res.cloudinary.com/demo/image/upload/sample.jpg"
        )

    def test_about_view_status_code(self):
        """Testin if view returns status 200"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_view_uses_correct_template(self):
        """ testing if views use the right HTML template"""
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about/about.html')

    def test_about_view_context_contains_image(self):
        """testing if views sends image in context """
        response = self.client.get(reverse('about'))
        images = response.context['images']
        self.assertEqual(len(images), 1)
        self.assertIn("sample", str(images[0].image))
