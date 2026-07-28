from django.shortcuts import render,redirect,get_object_or_404
from app1.models import Customer,Product
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
# Create your views here.

class HomePage(ListView):
    model = Customer
    template_name='customer/customer_page.html'
    context_object_name='home'

class AddPage(CreateView):
    model = Customer
    fields="__all__"
    template_name='customer/add_customer.html'
    success_url=reverse_lazy('home')

class UpdatePage(UpdateView):
    model= Customer
    fields="__all__"
    template_name='customer/update_customer.html'
    success_url=reverse_lazy('home')

class DeletePage(DeleteView):
    model = Customer
    template_name = 'customer/delete_customer.html'
    success_url = reverse_lazy('home')

class ProductPage(ListView):
    model = Product
    template_name='product/product_page.html'
    context_object_name='product'

class AddProductPage(CreateView):
    model = Product
    fields=['product_name','category','price','quantity']
    template_name='product/add_product.html'
    success_url=reverse_lazy('product')

class UpdateProductPage(UpdateView):
    model= Product
    fields=['product_name','category','price','quantity']
    template_name='product/update_product.html'
    success_url=reverse_lazy('product')

class DeleteProductPage(DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('product')