from django.urls import path
from . import views #import views

urlpatterns = [
    path('', views.manage, name="management"), #root dir
    path('changehours', views.changeHours, name="change_hours"),
    path('settings', views.settings, name="settings"),
    path('save_data', views.save_data, name="save_data"),
    path('changeabout', views.changeAbout, name="change_about"),
    path('add_a_product', views.add_a_product, name="add_a_product"),
]
