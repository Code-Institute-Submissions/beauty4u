from django.contrib import admin
from django.urls import path
from . import views #import home views 

urlpatterns = [
    path('', views.index, name="home"), #root dir
]
