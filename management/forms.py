from django import forms 
from home.models import openHours, aboutUs
from management.models import Staff, Coupons
from products.models import Product

class HoursForm(forms.ModelForm):
    """ A form to render model fields for opening time changes """
    class Meta:
        model = openHours
        fields = [
            'day',
            'openingTime',
            'closingTime',
            'markedClosed',
        ]


    def __init__(self, *args, **kwargs):
            """ Style the form """ 

            super().__init__(*args, **kwargs)

            placeholders = {
                'day': 'Select Day',
                'openingTime': 'Select Opening Time',
                'closingTime': 'Select Closing Time',
                'markedClosed':'Open/Closed',
                }

            for field in self.fields:
                if self.fields[field].required:
                    placeholder = f' {placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields["markedClosed"].widget.attrs['data-toggle'] = "toggle"
                self.fields["markedClosed"].widget.attrs['data-onstyle'] = "success"
                self.fields["markedClosed"].widget.attrs['data-offstyle'] = "danger"
                self.fields["markedClosed"].widget.attrs['data-on'] = "Yes"
                self.fields["markedClosed"].widget.attrs['data-off'] = "No"
                self.fields[field].label = False 

class aboutForm(forms.ModelForm):
    """ A form to render model fields for opening time changes """
    class Meta:
        model = aboutUs
        fields = [
            'content',
        ]  



class staffForm(forms.ModelForm):
    """ A form to render model fields for opening time changes """
    class Meta:
        model = Staff
        fields = [
            'name',
            'position',
            'available',
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



class couponForm(forms.ModelForm):
    """ A form to render model fields for opening time changes """
    class Meta:
        model = Coupons
        fields = [
            'name',
            'code',
            'discount',
            'active',
        ]                



