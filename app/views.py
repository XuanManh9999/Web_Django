from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {}
    return render(request, 'app/home.html', context)

def cart(request):
    context = {}
    return render(request, 'app/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'app/checkout.html', context)

def login(request):
    context = {}
    return render(request, 'auth/login.html', context)
def register(request):
    context = {}
    return render(request, 'auth/register.html', context)

def forgot_password(request):
    context = {}
    return render(request, 'auth/forgot_password.html', context)