from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from about.models import TeamModel, TestimonialModel


class AllTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(TeamModel)
class TeamModelAmin(AllTranslationAdmin):
    list_display = ['name', 'position', 'created_at']
    search_fields = ['name', 'position', 'about']
    list_filter = ['position', 'created_at']


@admin.register(TestimonialModel)
class TeamModelAmin(AllTranslationAdmin):
    list_display = ['name', 'job', 'created_at']
    search_fields = ['name', 'job', 'feedback']
    list_filter = ['job', 'created_at']
