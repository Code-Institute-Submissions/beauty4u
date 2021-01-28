from django.contrib import admin
from .models import Product, Category, Brand, Review 

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
        'in_stock', 
        'featured_product',

    )

    ordering = ('name',)



class CategoryAdmin(admin.ModelAdmin):

    list_display =(
        'name',
    )

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Review)
