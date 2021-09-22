from modeltranslation.translator import register, TranslationOptions

from blog.models import BlogCategoryModel, BlogTagsModel, BlogAuthorModel, BlogModel


@register(BlogCategoryModel)
class BlogCategoryTranslationOption(TranslationOptions):
    fields = ('title',)


@register(BlogTagsModel)
class BlogTagsTranslationOption(TranslationOptions):
    fields = ('title',)


@register(BlogAuthorModel)
class BlogAuthorTranslationOption(TranslationOptions):
    fields = ('first_name', 'last_name',)


@register(BlogModel)
class BlogTranslationOption(TranslationOptions):
    fields = ('title', 'little_about', 'full_about',)

