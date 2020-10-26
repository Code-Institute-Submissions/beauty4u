from django.urls import path
from . import views #import home views 

urlpatterns = [
    path('', views.view_cart, name="view_cart"), #root dir
    path('add/<item_id>', views.add_to_cart, name="add_to_cart"), #root dir
]
