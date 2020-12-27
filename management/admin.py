from django.contrib import admin
from .models import Sitesettings, Staff, Coupons

# Register your models here.
admin.site.register(Sitesettings)
admin.site.register(Staff)
admin.site.register(Coupons)
