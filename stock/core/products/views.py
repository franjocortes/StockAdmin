from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from core.products.forms import ProductForm
from core.products.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos'
        context['count'] = Product.objects.all().count()
        return context


class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/form.html'
    success_url = reverse_lazy('products:product-list')
    success_message = 'El producto se registró correctamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Producto'
        context['back_url'] = self.success_url
        return context


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/form.html'
    success_url = reverse_lazy('products:product-list')
    success_message = 'El producto se modificó correctamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modificar Producto'
        context['back_url'] = self.success_url
        return context

class ProductDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:product-list')
    success_message = 'El producto se eliminó correctamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Producto'
        context['back_url'] = self.success_url
        return context
