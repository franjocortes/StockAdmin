from django.contrib import admin

# Register your models here.
from core.products.models import Category

admin.site.register(Category)
