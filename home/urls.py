from django.urls import path
from . import views #import home views 

urlpatterns = [
    path('', views.index, name="home"), #root dir
    path('contact', views.contact, name="contact"), #root dir
]
