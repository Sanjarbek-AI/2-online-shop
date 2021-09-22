from django.contrib import admin

from users.models import ProfileModel


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name']
    list_filter = ['first_name']

