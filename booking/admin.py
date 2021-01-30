from django.contrib import admin
from .models import Bookings, serviceCategory, Services


class BookingsAdmin(admin.ModelAdmin):

    model = Bookings

    readonly_fields = ('booking_id', 'customer_name',
                       'service', 'username',
                       'date', 'time', 'staff',)

    fields = ('booking_id', 'customer_name',
              'service', 'username',
              'date', 'time', 'staff', 'confirmed',)


admin.site.register(Bookings, BookingsAdmin)
admin.site.register(serviceCategory)
admin.site.register(Services)
