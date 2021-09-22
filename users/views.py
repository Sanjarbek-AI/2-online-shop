from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView

from users.forms import ProfileModelForm
from users.models import ProfileModel


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileModelForm
    template_name = 'user-acount.html'

    def get_object(self, queryset=None):
        profile, create = ProfileModel.objects.get_or_create(user=self.request.user)
        return profile

    def get_success_url(self):
        return reverse('user:profile')


def password_change(request):
    return redirect(reverse('user:profile'))