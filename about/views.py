from django.views.generic import TemplateView

from about.models import TeamModel


class AboutTemplateView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        context['team_members'] = TeamModel.objects.all()
        return context
