
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_new_orders, name='new_orders' ),
    path('order/<str:pk>/', views.view_order, name='order'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('orders/', views.orders, name='orders'),
    path('customers/',views.customers, name='customers'),
    path('products', views.products, name='products'),
    path('product/<str:pk>/', views.product, name='product'),


    path('add_product/', views.add_product, name='add_product'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('add_order/', views.add_order, name='add_order'),
    # path('update_product/<str:pk>/', update_product, name="update_product"),
    # path('delete_product/<str:pk>/', delete_product, name="delete_product"),
   
]
