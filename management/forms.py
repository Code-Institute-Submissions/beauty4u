from django import forms
from home.models import openHours, aboutUs
from management.models import Staff, Coupons
from products.models import Product, Category, Brand
from booking.models import Services, serviceCategory
from .widgets import CustomClearableFileInput


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

        super().__init__(*args, **kwargs)

        placeholders = {
            'day': 'Select Day',
            'openingTime': 'Select Opening Time',
            'closingTime': 'Select Closing Time',
            'markedClosed': 'Open/Closed',
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


class addCategory(forms.ModelForm):
    """ A form to render model fields for opening time changes """
    class Meta:
        model = Category
        fields = [
            'name',
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Enter Category Name',
            }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class addBrand(forms.ModelForm):
    """ A form to render model fields for opening time changes """
    class Meta:
        model = Brand
        fields = [
            'brand',
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {
            'brand': 'Enter Brand Name',
            }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


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
            'featured_product'
        ]

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):

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
            'image': 'Select Image',
            'featured_product': 'Featured Product?'
            }

        self.fields['category'].widget.attrs['autofocus'] = True
        self.fields['category'].empty_label = "Select A Category"
        self.fields['brand'].empty_label = "Select A Brand"
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f' {placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'add-product-input'
            self.fields[field].label = False


class updateProduct(forms.ModelForm):
    """ A form to render model fields for opening time changes """
    class Meta:
        model = Product
        fields = [
            'in_stock',
            'featured_product',
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
    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {
            'in_stock': 'Manage Stock',
            'featured_product': 'Featured Product?',
            'category': 'Select Product Category',
            'brand': 'Select Product Category',
            'sku': 'Product Sku',
            'name': 'Product Name',
            'description': 'Enter Product Description',
            'price': 'Price',
            'sale_price': 'Sale Price',
            'size': 'Size',
            'image': 'Select Image',

            }

        self.fields['category'].widget.attrs['autofocus'] = True
        self.fields['in_stock'].widget.attrs['class'] = 'make-label-bold'
        self.fields['category'].empty_label = "Select A Category"
        self.fields['brand'].empty_label = "Select A Brand"
        self.fields['featured_product'].empty_label = "Featured Product?"
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f' {placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'add-product-input'


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


class addServiceForm(forms.ModelForm):
    """ A form to render model fields for opening time changes """
    class Meta:
        model = Services
        fields = [
            'name',
            'price',
            'serviceCategory'
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Enter Service Name',
            'price': 'Enter Service price',
            'serviceCategory': 'Choose Category',
            }

        self.fields['serviceCategory'].empty_label = "Select A Category"
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class addServiceCategoryForm(forms.ModelForm):
    """ A form to render model fields for opening time changes """
    class Meta:
        model = serviceCategory
        fields = [
            'name',
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Enter Service Category Name',

            }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
