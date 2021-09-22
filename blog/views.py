from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import BlogCommentModelForm
from blog.models import BlogModel, BlogCategoryModel, BlogTagsModel


class BlogListView(ListView):
    model = BlogModel
    context_object_name = 'blogs'
    template_name = 'blogs.html'
    paginate_by = 5

    def get_queryset(self):
        qs = BlogModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')

        if tag:
            qs = qs.filter(tags__in=tag)
        if cat:
            qs = qs.filter(category_id=cat)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['categories'] = BlogCategoryModel.objects.all()
        context['tags'] = BlogTagsModel.objects.all()
        context['recent_blogs'] = BlogModel.objects.order_by('-pk')[:2]
        return context


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blog-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = BlogTagsModel.objects.all()
        context['recent_blogs'] = BlogModel.objects.order_by('-pk')[:3]
        return context


class BlogCommentCreateView(CreateView):
    form_class = BlogCommentModelForm
    template_name = 'blog-detail.html'

    def form_valid(self, form):
        form.instance.blog = get_object_or_404(BlogModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.kwargs.get('pk')})
