from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_details, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]