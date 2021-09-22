from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from blog.models import BlogCategoryModel, BlogTagsModel, BlogAuthorModel, BlogModel, BlogCommentModel


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


@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(AllTranslationAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(BlogTagsModel)
class BlogTagsModelAdmin(AllTranslationAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(BlogAuthorModel)
class BlogAuthorModelAdmin(AllTranslationAdmin):
    list_display = ['first_name', 'last_name', 'created_at']
    search_fields = ['first_name', 'last_name']
    list_filter = ['created_at']


@admin.register(BlogModel)
class BlogModelAdmin(AllTranslationAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'little_about', 'full_about']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['blog_views']
    autocomplete_fields = ['tags']


@admin.register(BlogCommentModel)
class BlogCommentModelAdmin(admin.ModelAdmin):
    list_display = ['comment']
    search_fields = ['comment']
    list_filter = ['submitted_at']
