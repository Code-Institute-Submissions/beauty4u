from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.

class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)




class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine),

    readonly_fields = ('order_number', 'date', 
        'delivery_cost', 'subtotal', 
        'total', 'original_cart', 'stripe_pid')

    fields = ('order_number', 'date', 'full_name', 'email',
               'phone_number', 'street_address1', 'street_address2', 
               'town_or_city', 'county', 'country', 
               'postcode', 'delivery_cost', 'shipping_method',
               'subtotal', 'total', 'original_cart', 'stripe_pid'
        )

    list_display = ('order_number', 'date', 'full_name',
                    'subtotal', 'delivery_cost', 'total'
                    )

    #Put most recent orders at the top of the list
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)