from django.urls import path
from . import views

urlpatterns = [
    path('cart-details', views.cart_details, name='cart'),
]