from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from products.models import ProductModel

UserModel = get_user_model()


class OrderModel(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='order',
        verbose_name=_('User')
    )

    products = models.ManyToManyField(
        ProductModel,
        related_name='orders',
        verbose_name=_('Products')
    )

    full_name = models.CharField(max_length=30, verbose_name=_('First Name'))
    address = models.CharField(max_length=30, verbose_name=_('Address'))
    city = models.CharField(max_length=30, verbose_name=_('City'))
    phone = models.CharField(max_length=30, verbose_name=_('Phone'))
    email = models.EmailField(verbose_name=_('Email'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
