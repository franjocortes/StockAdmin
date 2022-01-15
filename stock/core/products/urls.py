from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import ProductListView

app_name = 'products'

urlpatterns = [
    path('', login_required(ProductListView.as_view()), name='product-list'),
]