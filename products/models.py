from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254) # Must provide a name
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__ (self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Brand(models.Model):
    brand = models.CharField(max_length=254) # Must provide a name 
    logo_url = models.URLField(max_length=1024, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    def __str__ (self):
        return self.brand


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    in_stock = models.BooleanField(default=True, null=True, blank=True)
    size = models.CharField(max_length=254, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    featured_product = models.BooleanField(default=False, null=True, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name         

