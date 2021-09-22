from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from products.forms import ProductCommentModelForm
from products.models import ProductModel, ProductCategoryModel, ProductBrandModel, ProductTagsModel, ProductColorModel


class ProductListView(ListView):
    template_name = 'products-list.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')

        if cat:
            qs = qs.filter(categories__id=cat)
        if brand:
            qs = qs.filter(brand_id=brand)
        if tag:
            qs = qs.filter(tags__id=tag)
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategoryModel.objects.all()
        context['brands'] = ProductBrandModel.objects.all()
        context['tags'] = ProductTagsModel.objects.all()
        context['colors'] = ProductColorModel.objects.all()
        return context


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_products'] = ProductModel.objects.order_by('-pk')[:3]
        return context


class WishListView(LoginRequiredMixin, ListView):
    template_name = 'user-wishlist.html'
    context_object_name = 'products'

    def get_queryset(self):
        return self.request.user.wishlist.all()


@login_required
def add_wishlist(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    user = request.user

    if user in product.wishlist.all():
        product.wishlist.remove(user)
    else:
        product.wishlist.add(user)

    return redirect(request.GET.get('next', '/'))


def add_to_cart(request, pk):
    cart = request.session.get('cart', [])

    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session['cart'] = cart

    return redirect(request.GET.get('next', '/'))


class CartListView(ListView):
    template_name = 'product-cart.html'
    context_object_name = 'products'

    def get_queryset(self):
        return ProductModel.get_from_cart(self.request)


class ProductCommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'product-detail.html'
    form_class = ProductCommentModelForm

    def form_valid(self, form):
        form.instance.blog = get_object_or_404(ProductModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.kwargs.get('pk')})
