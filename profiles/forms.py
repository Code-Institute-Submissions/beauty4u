from django import forms 
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Style the form """ 

        super().__init__(*args, **kwargs)

        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town/City',
            'default_postcode': 'Post Code',
            'default_county': 'County',
            'default_country': 'Country'
            }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f' {placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False

