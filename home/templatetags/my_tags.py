from django import template
from django.db.models import Sum

from products.models import ProductModel

register = template.Library()


@register.filter
def in_wishlist(product, request):
    return request.user in product.wishlist.all()


@register.filter
def in_cart(product, request):
    return product.pk in request.session.get('cart', [])


@register.simple_tag
def cart_products(request):
    return len(request.session.get('cart', []))


@register.simple_tag
def cart_price(request):
    if cart_products(request) == 0:
        return 0

    return ProductModel.get_from_cart(request).aggregate(
        Sum('price')
    )['price__sum']
