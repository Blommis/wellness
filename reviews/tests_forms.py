from django.test import TestCase
from reviews.forms import ReviewForm


class ReviewFormTest(TestCase):
    def setUp(self):
        """Sets up formdata for testes"""
        self.valid_data = {
            'rating': 5,
            'comment': 'Excellent product!'
        }

    def test_review_form_valid_data(self):
        """form should be correct with right data"""
        form = ReviewForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_review_form_missing_rating(self):
        """user must rate to leave a review"""
        data = self.valid_data.copy()
        data['rating'] = ''
        form = ReviewForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)

    def test_review_form_missing_comment(self):
        """user must comment to leave a review"""
        data = self.valid_data.copy()
        data['comment'] = ''
        form = ReviewForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors)

    def test_review_form_widgets(self):
        """Formu should use widgets"""
        form = ReviewForm()
        self.assertIn('form-select',
                      form.fields['rating'].widget.attrs['class'])
        self.assertIn('form-control',
                      form.fields['comment'].widget.attrs['class'])
