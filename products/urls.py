from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('view/<product_id>', views.product_detail, name="product_detail"),
    path('add_review', views.add_review, name="add_review"),
]
