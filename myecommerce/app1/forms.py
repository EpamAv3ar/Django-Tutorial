from django import forms
from models import Customer,Product

class CustomerForm(forms.ModelFormform):
    class Meta:
      model = Customer
      fields ="__all__"

class ProductForm(forms.ModelFormform):
    class Meta:
      model = Product
      fields ="__all__"