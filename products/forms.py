from django import forms

from products.models import ProductColorModel, ProductCommentModel


class ProductColorModelForm(forms.ModelForm):
    class Meta:
        model = ProductColorModel
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={
                'type': 'color'
            })
        }


class ProductCommentModelForm(forms.ModelForm):
    class Meta:
        model = ProductCommentModel
        exclude = ['submitted_at', 'product']
