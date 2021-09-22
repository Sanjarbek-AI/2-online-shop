from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from about.models import TestimonialModel
from home.forms import NewsletterModelForm
from products.models import ProductModel


class HomeTemplateView(TemplateView):
    template_name = 'layouts/base-1.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['testimonials'] = TestimonialModel.objects.all()
        context['samsung'] = ProductModel.objects.filter(brand_id=1)
        context['lg'] = ProductModel.objects.filter(brand_id=3)
        context['acer'] = ProductModel.objects.filter(brand_id=7)
        return context


class NewsletterMemberCreateView(CreateView):
    form_class = NewsletterModelForm
    template_name = 'layouts/base-1.html'

    def get_success_url(self):
        return reverse('home:home')
