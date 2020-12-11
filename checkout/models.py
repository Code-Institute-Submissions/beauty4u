import uuid
from django.db.models import Sum
from django.conf import settings
from django.db import models
from products.models import Product

# Create your models here.
class Order(models.Model):
 
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50,  null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=40, null=True, blank=True) #not required
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True) #not required
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)


    def update_total(self):
        """ Update total each time a new line item is added """
        self.subtotal = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.subtotal < settings.FREE_SHIPPING_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY_COST
        else:
            self.delivery_cost = 0
        self.total = self.subtotal + self.delivery_cost        
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