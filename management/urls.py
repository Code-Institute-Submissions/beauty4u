from django.urls import path
from . import views #import views

urlpatterns = [
    path('', views.manage, name="management"), #root dir
    path('changehours', views.changeHours, name="change_hours"),
    path('settings', views.settings, name="settings"),
    path('staff', views.staff, name="staff"),
    path('bookings', views.bookings, name="bookings"),
    path('booking_details/<booking_id>', views.view_booking_details, name="view_booking_details"),
    path('update_booking_status', views.update_booking_status, name="update_booking_status"),
    path('update_staff_avail', views.update_staff_avail, name="update_staff_avail"),
    path('remove_staff', views.remove_staff, name="remove_staff"),
    path('remove_service', views.remove_service, name="remove_service"),
    path('remove_service_category', views.remove_service_category, name="remove_service_category"),
    path('view_orders', views.view_orders, name="view_orders"),
    path('orders/<order_number2>', views.order_detail, name="order_detail"),
    path('save_data', views.save_data, name="save_data"),
    path('changeabout', views.changeAbout, name="change_about"),
    path('add_a_product', views.add_a_product, name="add_a_product"),
    path('add_a_category', views.add_a_category, name="add_a_category"),
    path('add_a_brand', views.add_a_brand, name="add_a_brand"),
    path('delete_a_brand', views.delete_a_brand, name="delete_a_brand"),
    path('delete_a_category', views.delete_a_category, name="delete_a_category"),
    path('delete_product', views.delete_product, name="delete_product"),
    path('coupons', views.coupons, name="coupons"),
    path('update_coupon_active', views.update_coupon_active, name="update_coupon_active"),
    path('manage_products', views.manage_products, name="manage_products"),
    path('manage_specific_product/<product_name>', views.manage_specific_product ,name="manage_specific_product"),
    path('update_coupon_minspend', views.update_coupon_minspend, name="update_coupon_minspend"),
    path('send_marketing_email', views.send_marketing_email, name="send_marketing_email"),
    path('addService', views.addService, name="addService"),
    path('addServiceCategory', views.addServiceCategory, name="addServiceCategory"),
     
    
]
