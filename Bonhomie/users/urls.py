from django.urls import path
from . import views

urlpatterns = [
    path('user-login', views.login_user, name="log-in"),
    path('register/', views.register_user, name="register-user"),
]