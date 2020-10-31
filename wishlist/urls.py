from django.urls import path
from . import views #import home views 

urlpatterns = [
    path('', views.view_wishlist, name="view_wishlist"), #root dir
]
