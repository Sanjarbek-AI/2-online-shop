from django.urls import path

from users.views import ProfileUpdateView, password_change

app_name = 'user'

urlpatterns = [
    path('', ProfileUpdateView.as_view(), name='profile'),
    path('accounts/password/change/done/', password_change, name='password'),
]
