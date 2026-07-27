from django.contrib import admin
from django.urls import path
from app1.views import (
    HomePage,
    AddPage,
    UpdatePage,
    DeletePage,
    ProductPage,
    AddProductPage,
    UpdateProductPage,
    DeleteProductPage
)

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('addcustomer/',AddPage.as_view(),name='addpage'),
    path('updatecustomer/<int:pk>/',UpdatePage.as_view(),name='updatepage'),
    path('deletecustomer/<int:pk>',DeletePage.as_view(),name='deletepage'),
    path('viewproduct/',ProductPage.as_view(),name='product'),
    path('addproduct/',AddProductPage.as_view(),name='addproduct'),
    path('updateproduct/<int:pk>/',UpdateProductPage.as_view(),name='updateproduct'),
    path('deleteproduct/<int:pk>/',DeleteProductPage.as_view(),name='deleteproduct'),

]
