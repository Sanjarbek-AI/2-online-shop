from django.db import models
from django.utils.translation import ugettext_lazy as _


class NewsletterModel(models.Model):
    email = models.EmailField(verbose_name=_('Email'))
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Joined At'))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Newsletter Member')
        verbose_name_plural = _('Newsletter Members')
