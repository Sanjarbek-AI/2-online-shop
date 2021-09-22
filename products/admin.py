from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from products.forms import ProductColorModelForm
from products.models import ProductCategoryModel, ProductColorModel, ProductTagsModel, ProductBrandModel, ProductModel, \
    ProductImageModel, ProductSizeModel


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


@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(AllTranslationAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(ProductColorModel)
class ProductColorModelAdmin(AllTranslationAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(ProductTagsModel)
class ProductTagsModelAdmin(AllTranslationAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(ProductBrandModel)
class ProductBrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(ProductSizeModel)
class ProductBrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductModeAdmin(AllTranslationAdmin):
    list_display = ['title', 'price', 'created_at', 'updated_at']
    search_fields = ['title', 'little_about', 'full_about']
    list_filter = ['created_at']
    readonly_fields = ['product_views', 'wishlist']
    autocomplete_fields = ['colors', 'tags', 'categories', 'sizes']
    inlines = [ProductImageStackedInline]
