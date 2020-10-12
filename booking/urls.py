from django.urls import path
from . import views #import home views 

urlpatterns = [
    path('', views.booking, name="booking"), 

]
