from django.db import models

# Create your models here.
class Services(models.Model):

    class Meta:
        verbose_name_plural = "Services"


    serviceCategory = models.ForeignKey('ServiceCategory', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name 


class serviceCategory(models.Model):

    class Meta:
        verbose_name_plural = "Service Categories"

    name = models.CharField(max_length=254)
   
    def __str__(self):
        return self.name 


class Bookings(models.Model):

    class Meta:
        verbose_name_plural = "Bookings"

    username = models.CharField(max_length=254, null=True, blank=True)
    customer_name = models.CharField(max_length=254, null=True, blank=True)
    service = models.CharField(max_length=254, null=True, blank=True)
    time = models.CharField(max_length=254, null=True, blank=True)
    
    
    def __str__(self):
        return self.customer_name