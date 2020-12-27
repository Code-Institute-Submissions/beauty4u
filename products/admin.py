from django.contrib import admin
from .models import Product, Category, Brand 

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """ This class will determine the fields that will display in the admin panel"""
    list_display = (
        'sku',
        'name',
        'brand',
        'category',
        'size',
        'price',
        'rating',
        'image',
        'in_stock'

    )

    ordering = ('name',)



class CategoryAdmin(admin.ModelAdmin):

    list_display =(
        'friendly_name',
        'name',
    )

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'logo',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)