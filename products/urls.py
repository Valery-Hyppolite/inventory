
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
    path('update_product/<str:pk>/', views.update_product, name="update_product"),
    path('delete_product/<str:pk>/', views.delete_product, name="delete_product"),
    path('update_customer/<str:pk>/', views.update_customer, name="update_customer"),
    path('delete_customer/<str:pk>/', views.delete_customer, name="delete_customer"),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('update_orderitem/<str:pk>/', views.update_orderitem, name="update_orderitem"),
    path('update_shipping/<str:pk>/', views.update_shipping, name="update_shipping"),
]
