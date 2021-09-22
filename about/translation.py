from modeltranslation.translator import register, TranslationOptions

from about.models import TeamModel, TestimonialModel


@register(TeamModel)
class TeamModelTranslationOption(TranslationOptions):
    fields = ('name', 'position', 'about',)


@register(TestimonialModel)
class TeamModelTranslationOption(TranslationOptions):
    fields = ('name', 'job', 'feedback',)
