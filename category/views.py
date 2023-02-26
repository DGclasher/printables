from .models import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required()
def add_to_cart(request, pk):
    products = Product.objects.get(pk=pk)
    ncart = Cart.objects.create(user=request.user, products=products)
    ncart.save()
    return HttpResponseRedirect(reverse("products"))

@login_required()
def remove_from_cart(request, pk):
    products = Product.objects.get(pk=pk)
    ncart = Cart.objects.get(products=products)
    ncart.delete()
    return HttpResponseRedirect(reverse("cart"))

@login_required()
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = 0
    for cart_item in cart_items:
        total_price += cart_item.products.price
    return render(request, 'cart.html', {"cart_items" : cart_items, "total_price" : total_price})
    pass
