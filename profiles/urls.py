from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('my_orders', views.my_orders, name="my_orders"),
    path('my_bookings', views.my_bookings, name="my_bookings"),
    path('view_order/<order_number>', views.view_order, name="view_order"),
]
