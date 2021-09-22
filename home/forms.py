from django import forms

from home.models import NewsletterModel


class NewsletterModelForm(forms.ModelForm):
    class Meta:
        model = NewsletterModel
        fields = ['email']
