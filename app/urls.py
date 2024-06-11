from django.contrib import admin
from django.urls import path
#import trong chinh thu muc do luon
from . import views

urlpatterns = [
    path('', views.home),
]