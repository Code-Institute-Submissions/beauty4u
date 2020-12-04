from django.db import models

# Create your models here.
class openHours(models.Model):

    class Meta:
        verbose_name_plural = "Opening Hours"

    day = models.CharField(max_length=254, null=True, blank=True)
    openingTime = models.TimeField(auto_now=False, null=True)
    closingTime = models.TimeField(auto_now=False, null=True)
    
    def __str__(self):
        return self.day
