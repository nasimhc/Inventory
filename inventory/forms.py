# from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta():
        model = Product
        fields = ['brand' ,'name', 'shade', 'price', 'quantity', 'description', 'product_image']
        labels = {
                    'brand': '',
                    'name': '',
                    'shade': '',
                    'price': '',
                    'quantity': '',
                    'description': '',
                    'product_image': ''
                }
        widgets = {
            'brand': forms.Select(attrs={'class': 'md:w-80 py-2 px-4 outline-none rounded-xl mt-2 mb-2 text-gray-500 focus:ring-1 focus:ring-orange-200', 'placeholder': 'Product Brand'}),

            'name': forms.TextInput(attrs={'class': 'md:w-80 py-2 px-4 outline-none rounded-xl mt-2 mb-2 text-gray-500 focus:ring-1 focus:ring-orange-200', 'placeholder': 'Product Name', 'autocomplete':'off'}),

            'shade': forms.TextInput(attrs={'class': 'md:w-80 py-2 px-4 outline-none rounded-xl mt-2 mb-2 text-gray-500 focus:ring-1 focus:ring-orange-200', 'placeholder': 'Shade', 'autocomplete':'off'}),

            'price': forms.NumberInput(attrs={'class': 'md:w-80 py-2 px-4 outline-none rounded-xl mt-2 mb-2 text-gray-500 focus:ring-1 focus:ring-orange-200', 'placeholder': 'Price', 'autocomplete':'off'}),

            'quantity': forms.TextInput(attrs={'class': 'md:w-80 py-2 px-4 outline-none rounded-xl mt-2 mb-2 text-gray-500 focus:ring-1 focus:ring-orange-200', 'placeholder': 'Quantity', 'autocomplete':'off'}),

            'description': forms.Textarea(attrs={'class': 'md:w-80 py-2 px-4 outline-none rounded-xl mt-2 mb-2 text-gray-500 focus:ring-1 focus:ring-orange-200', 'placeholder': 'Product Description', 'rows': '4', 'autocomplete':'off'}), 
        }
