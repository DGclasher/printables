from .models import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required()
def add_to_cart(request, pk):
    products = Product.objects.get(pk=pk)
    ncart = Cart.objects.create(user=request.user, products=products)
    ncart.save()
    return redirect('/')

@login_required()
def remove_from_cart(request, pk):
    products = Product.objects.get(pk=pk)
    ncart = Cart.objects.get(products=products)
    ncart.delete()
    return redirect('/')

@login_required()
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    
    pass
