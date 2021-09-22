from django.contrib import admin

from home.models import NewsletterModel


@admin.register(NewsletterModel)
class NewsletterModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'joined_at']
    search_fields = ['email']
    list_filter = ['joined_at']
