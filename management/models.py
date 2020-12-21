from django.db import models

# Create your models here.
class Sitesettings(models.Model):

    class Meta:
        verbose_name_plural = 'Site Settings'

    name = models.CharField(max_length=250, null=True, blank=True, default="Free Shipping Treshold")
    status = models.BooleanField(default=True, null=True, blank=True)
    value = models.DecimalField(max_digits=5, null=True, blank=True, default="50.00", decimal_places=2)
    description  = models.TextField(max_length=250, null=True, blank=False)
    
    def __str__ (self):
        return self.name