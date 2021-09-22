from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView

from orders.forms import OrderModelForm
from products.models import ProductModel


class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'product-checkout.html'
    form_class = OrderModelForm
    success_url = '/'

    def form_valid(self, form):
        products = ProductModel.get_from_cart(self.request)
        form.instance.user = self.request.user
        order = form.save()
        order.products.set(products)
        order.save()

        self.request.session['cart'] = []
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.get_from_cart(self.request)
        return context
