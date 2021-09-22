from django.contrib import admin

from contact.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'sent_at']
    search_fields = ['name', 'subject', 'message']
    list_filter = ['sent_at', 'name']
