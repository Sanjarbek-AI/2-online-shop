from modeltranslation.translator import register, TranslationOptions

from products.models import ProductCategoryModel, ProductTagsModel, ProductColorModel, ProductBrandModel, ProductModel


@register(ProductCategoryModel)
class BlogCategoryTranslationOption(TranslationOptions):
    fields = ('title',)


@register(ProductTagsModel)
class BlogTagsTranslationOption(TranslationOptions):
    fields = ('title',)


@register(ProductColorModel)
class BlogTagsTranslationOption(TranslationOptions):
    fields = ('title',)


@register(ProductModel)
class ProductTranslationOption(TranslationOptions):
    fields = ('title', 'little_about', 'full_about',)
