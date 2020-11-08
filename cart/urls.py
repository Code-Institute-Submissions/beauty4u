from django.urls import path
from . import views #import home views 

urlpatterns = [
    path('', views.view_cart, name="view_cart"), #root dir
    path('add/<item_id>', views.add_to_cart, name="add_to_cart"), #root dir
    path('addtowishlist/<item_id>', views.add_wishlist_item_to_cart, name="add_wishlist_item_to_cart"),
    path('remove/<item_id>', views.adjust_cart, name="adjust_cart")
]
