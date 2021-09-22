from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class ProfileModel(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name=_('User')
    )

    first_name = models.CharField(max_length=30, verbose_name=_('First Name'), null=True, blank=True)
    last_name = models.CharField(max_length=30, verbose_name=_('Last Name'), null=True, blank=True)
    country = models.CharField(max_length=30, verbose_name=_('Country'), null=True, blank=True)
    address = models.CharField(max_length=30, verbose_name=_('Address'), null=True, blank=True)
    city = models.CharField(max_length=30, verbose_name=_('City'), null=True, blank=True)
    phone = models.CharField(max_length=30, verbose_name=_('Phone'), null=True, blank=True)
    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} | {self.last_name}'

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
