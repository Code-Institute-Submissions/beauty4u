from django.urls import path
from . import views #import home views 

urlpatterns = [
    path('', views.checkout, name="checkout"), #root dir
]
