from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),

path('collection/', views.collection, name='collection'),

path('weddings/', views.weddings, name='weddings'),

path('custom-orders/', views.custom_orders, name='custom_orders'),

path('order_success/',views.order_success,name='order_success'),

path('contact/', views.contact, name='contact'),

]