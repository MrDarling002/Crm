from django.db.models import deletion
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/',views.customers,name='customer'),
    path('product_category/',views.product_category,name='product_category'),
    path('order_status/', views.order_status,name="order_status"),
    path('service/',views.services,name="service"),
    path('customer/create',views.create_customer,name='create_customer'),
    path('orders-statuses/create',views.create_order_status,name='create_order_status'),
    path('products-brand/create',views.create_product_brand,name='create_product_brand'),
    path('product-category/create',views.create_product_brand,name='create_product_category'),
    path('services/create',views.create_service,name='create_service'),
    path('delete/<int:id>/',views.delete_order,name='delete_order'),
    path('delete_service/<int:id>/',views.delete_service,name='delete_service'),
    path('delete_category/<int:id>/',views.delete_category,name='delete_category'),
    path('delete_customer/<int:id>/',views.delete_customer,name='delete_customer'),
    path('delete_order_status/<int:id>/',views.delete_status,name='delete_order_status'),
    path('show/<int:id>',views.show,name='show'),
    path('product_category/<int:id>',views.show_category,name='show_category'),
    path('customer/<int:id>',views.show_customer,name='show_customer'),
    path('order_status/<int:id>',views.show_order_status,name='show_order_status'),
    path('service/<int:id>',views.show_service,name='show_service'),
    
]