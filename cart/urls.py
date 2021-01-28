from django.urls import path
from . import views 


urlpatterns = [
    path('add_to_cart', views.add_to_cart, name="add_to_cart"),
    path('refresh_cart', views.refresh_cart, name="refresh_cart"),
    path('change_shipping_method', views.change_shipping_method, name="change_shipping_method"),
    path('adjust_cart', views.adjust_cart, name="adjust_cart"),
   
]
