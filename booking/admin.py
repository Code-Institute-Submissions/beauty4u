from django.contrib import admin
from .models import Bookings, serviceCategory,Services

admin.site.register(Bookings)
admin.site.register(serviceCategory)
admin.site.register(Services)