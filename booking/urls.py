from django.urls import path
from . import views 

urlpatterns = [
    path('', views.booking, name="booking"), 
    path('select_staff', views.select_staff, name="select_staff"), 
    path('select_time', views.select_time, name="select_time"), 
    path('confirm_booking', views.confirm_booking, name="confirm_booking"), 
]
