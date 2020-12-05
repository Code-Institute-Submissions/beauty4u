from django import forms 
from home.models import openHours, aboutUs
from products.models import Product

class HoursForm(forms.ModelForm):
    """ A form to render model fields for opening time changes """
    class Meta:
        model = openHours
        fields = [
            'day',
            'openingTime',
            'closingTime',
        ]

class aboutForm(forms.ModelForm):
    """ A form to render model fields for opening time changes """
    class Meta:
        model = aboutUs
        fields = [
            'content',
        ]        


class addProductForm(forms.ModelForm):
    """ A form to render model fields for opening time changes """
    class Meta:
        model = Product
        fields = [
            'category',
            'brand',
            'sku',
            'name',
            'description',
            'price',
            'sale_price',
            'size', 
            'image',
        ]         