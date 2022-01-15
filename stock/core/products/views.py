from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from core.products.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'