from django import forms

from blog.models import BlogCommentModel


class BlogCommentModelForm(forms.ModelForm):
    class Meta:
        model = BlogCommentModel
        exclude = ['submitted_at', 'blog']
