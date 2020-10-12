from django.db import models

# Create your models here.
class Services(models.Model):

    class Meta:
        verbose_name_plural = "Services"


    service_category = models.ForeignKey('Service_Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name 


class Service_Category(models.Model):

    class Meta:
        verbose_name_plural = "Service Categories"

    name = models.CharField(max_length=254)
   
    def __str__(self):
        return self.name 


class Bookings(models.Model):

    class Meta:
        verbose_name_plural = "Bookings"

    customer_name = models.CharField(max_length=254)
    booking_made = models.DateTimeField(auto_now=True) 
    service = models.CharField(max_length=254)
    time = models.CharField(max_length=254)
    
    
    def __str__(self):
        return self.customer_name