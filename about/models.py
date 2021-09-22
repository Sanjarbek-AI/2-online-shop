from django.db import models
from django.utils.translation import ugettext_lazy as _


class TeamModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    position = models.CharField(max_length=50, verbose_name=_('Position'))
    about = models.TextField(verbose_name=_('About'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return f'{self.name} | {self.position}'

    class Meta:
        verbose_name = _('Team Member')
        verbose_name_plural = _('Team Members')


class TestimonialModel(models.Model):
    feedback = models.TextField(verbose_name=_('Feedback'))
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    job = models.CharField(max_length=50, verbose_name=_('Job'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return f'{self.name} | {self.job}'

    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

