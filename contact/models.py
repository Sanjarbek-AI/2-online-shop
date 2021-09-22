from django.db import models
from django.utils.translation import ugettext_lazy as _


class ContactModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))
    subject = models.CharField(max_length=255, verbose_name=_('Subject'), null=True, blank=True)
    message = models.TextField(verbose_name=_('Message'))
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Sent At'))

    def __str__(self):
        return f'{self.name} | {self.email}'

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

