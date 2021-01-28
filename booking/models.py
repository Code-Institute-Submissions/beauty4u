from django.db import models
import uuid

# Create your models here.
class Services(models.Model):

    class Meta:
        verbose_name_plural = "Services"


    serviceCategory = models.ForeignKey('ServiceCategory', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    

    def clean(self):
        """ Ensure Case Insensitive check on name """
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name 


class serviceCategory(models.Model):

    class Meta:
        verbose_name_plural = "Service Categories"

    name = models.CharField(max_length=254, unique=True)
   
    def clean(self):
        """ Ensure Case Insensitive check on name """
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name 


       


class Bookings(models.Model):

    class Meta:
        verbose_name_plural = "Bookings"

    booking_id = models.CharField(max_length=254, null=False, editable=False, default="")
    username = models.CharField(max_length=254, null=True, blank=True)
    customer_name = models.CharField(max_length=254, null=True, blank=True)
    service = models.CharField(max_length=254, null=True, blank=False)
    date = models.DateField(null=True, blank=False)
    time = models.CharField(max_length=254, null=True, blank=False)
    staff =  models.CharField(max_length=254, null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.username

    def _generate_booking_id(self):
        """ Generate order number """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """Make sure the order has an order number"""
        if not self.booking_id:
            self.booking_id= self._generate_booking_id()
        super().save(*args, **kwargs)