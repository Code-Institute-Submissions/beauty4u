from django.urls import path
from . import views #import home views 

urlpatterns = [
    path('', views.checkout, name="checkout"), #root dir
    path('checkout_success/<order_number>', views.checkout_success, name="checkout_success"), 
]
