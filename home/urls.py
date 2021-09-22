from django.urls import path

from home.views import HomeTemplateView, NewsletterMemberCreateView

app_name = 'home'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('subscribe/', NewsletterMemberCreateView.as_view(), name='subscribe'),
]