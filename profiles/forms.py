# profiles/forms.py
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_postcode',
            'default_town_or_city',
            'default_county',
            'default_country',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2 (optional)',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_country': 'Country',
        }

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
