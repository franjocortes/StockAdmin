from django.forms import *

from core.products.models import Product


class ProductForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for myform in self.visible_fields():
            myform.field.widget.attrs['class'] = 'form-control'

        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
