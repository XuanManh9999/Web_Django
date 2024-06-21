from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'app/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'items':0, 'order':0}
    context = {'items': items, 'order': order}
    return render(request, 'app/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'items': 0, 'order': 0}
    context = {'items': items, 'order': order}
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