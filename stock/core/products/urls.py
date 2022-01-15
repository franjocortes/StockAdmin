from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'products'

urlpatterns = [
    path('', login_required(ProductListView.as_view()), name='product-list'),
    path('new', login_required(ProductCreateView.as_view()), name='product-new'),
    path('edit/<int:pk>', login_required(ProductUpdateView.as_view()), name='product-edit'),
    path('delete/<int:pk>', login_required(ProductDeleteView.as_view()), name='product-delete'),
]
