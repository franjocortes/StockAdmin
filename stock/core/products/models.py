from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category list'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name='Categorías')
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Precio Unitario')
    stock = models.IntegerField(verbose_name='Stock')

    def __str__(self):
        return self.name
