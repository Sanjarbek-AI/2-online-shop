from django.urls import reverse
from django.views.generic import CreateView

from contact.forms import ContactModelForm


class ContactCreateView(CreateView):
    form_class = ContactModelForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact:create')
