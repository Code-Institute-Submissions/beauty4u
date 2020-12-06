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

    def __init__(self, *args, **kwargs):
            """ Style the form """ 

            super().__init__(*args, **kwargs)

            placeholders = {
                'category': 'Select Product Category',
                'brand': 'Select Product Category',
                'sku': 'Product Sku',
                'name': 'Product Name',
                'description': 'Enter Product Description',
                'price': 'Price',
                'sale_price': 'Sale Price',
                'size': 'Size',
                'image': 'Select Image'
                }

            self.fields['category'].widget.attrs['autofocus'] = True
            for field in self.fields:
                if self.fields[field].required:
                    placeholder = f' {placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'add-product-input'
                self.fields[field].label = False 