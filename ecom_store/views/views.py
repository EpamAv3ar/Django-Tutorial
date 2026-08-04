from django.shortcuts import render, redirect
from ecom_store.models import Product, Category, Customer

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_page(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product.html', {'product': product})
