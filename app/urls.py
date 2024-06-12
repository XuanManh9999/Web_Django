from django.contrib import admin
from django.urls import path
#import trong chinh thu muc do luon
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
]