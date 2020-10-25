from django.contrib import admin
from .models import Product, Category, Brand 

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """ This class will determine the fields that will display in the admin panel"""
    list_display = (
        'sku',
        'name',
        'category',
        'size',
        'price',
        'rating',
        'image',

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
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)