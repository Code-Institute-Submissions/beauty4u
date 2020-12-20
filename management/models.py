from django.db import models

# Create your models here.
class Webstats(models.Model):
    monday = models.IntegerField(null=True, blank=True)
    tuesday = models.IntegerField(null=True, blank=True)
    wednesday = models.IntegerField(null=True, blank=True)
    thursday = models.IntegerField(null=True, blank=True)
    friday = models.IntegerField(null=True, blank=True)
    saturday = models.IntegerField(null=True, blank=True)
    sunday = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name   