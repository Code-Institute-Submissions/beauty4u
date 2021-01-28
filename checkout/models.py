import uuid
from django.db.models import Sum
from django.conf import settings
from django.db import models
from products.models import Product
from django_countries.fields import CountryField
from management.models import Sitesettings
from django.shortcuts import get_object_or_404
from profiles.models import UserProfile



# Create your models here.
class Order(models.Model):
 
    order_number = models.CharField(max_length=254, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    full_name = models.CharField(max_length=254,  null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=254, null=False, blank=False)
    street_address1 = models.CharField(max_length=254, null=False, blank=False)
    street_address2 = models.CharField(max_length=254, null=False, blank=False)
    town_or_city = models.CharField(max_length=254, null=False, blank=False)
    county = models.CharField(max_length=254, null=True, blank=True) #not required
    country = CountryField(max_length=254, blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=254, null=True, blank=True) #not required
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    shipping_method = models.CharField(max_length=254,  null=True, blank=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')


    def update_total(self):
        """ Update total each time a new line item is added """
        self.save()

    def _generate_order_number(self):
        """ Generate order number """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """Make sure the order has an order number"""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order_number



class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.name} on order {self.order.order_number}'