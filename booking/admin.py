from django.contrib import admin
from .models import Bookings, Service_Category,Services

admin.site.register(Bookings)
admin.site.register(Service_Category)
admin.site.register(Services)