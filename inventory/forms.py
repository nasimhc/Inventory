from dataclasses import field
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta():
        model = Product
        fields = ['brand' ,'name', 'shade', 'price', 'quantity', 'description']
