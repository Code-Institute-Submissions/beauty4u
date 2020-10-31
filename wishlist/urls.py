from django.urls import path
from . import views #import home views 

urlpatterns = [
    path('', views.view_wishlist, name="view_wishlist"), #root dir
    path('add/<item_id>', views.add_to_wishlist, name="add_to_wishlist"), #root dir
]
