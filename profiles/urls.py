from django.urls import path
from . import views #import views

urlpatterns = [
    path('', views.profile, name="profile"), #root dir    
]
