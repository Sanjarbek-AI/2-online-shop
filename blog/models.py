from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BlogCategoryModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Category Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Category Created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Blog Category')
        verbose_name_plural = _('Blog Categories')


class BlogTagsModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Tag Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Tag Created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Blog Tag')
        verbose_name_plural = _('Blog Tags')


class BlogAuthorModel(models.Model):
    image = models.ImageField(upload_to='Blog Authors', verbose_name=_('Author Image'))
    first_name = models.CharField(max_length=255, verbose_name=_('Author FirstName'))
    last_name = models.CharField(max_length=255, verbose_name=_('Author LastName'))
    job = models.CharField(max_length=50, verbose_name=_('Author Job'), null=True, blank=True)
    about = models.TextField(verbose_name=_('About Author'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Author Created'))

    def __str__(self):
        return f'{self.first_name} | {self.last_name}'

    class Meta:
        verbose_name = _('Blog Author')
        verbose_name_plural = _('Blog Authors')


class BlogModel(models.Model):
    category = models.ForeignKey(
        BlogCategoryModel,
        on_delete=models.CASCADE,
        related_name='blogs',
        verbose_name=_('Category')
    )

    author = models.ForeignKey(
        BlogAuthorModel,
        on_delete=models.CASCADE,
        related_name='blogs',
        verbose_name=_('Author')
    )

    tags = models.ManyToManyField(
        BlogTagsModel,
        related_name='blogs',
        verbose_name=_('Tags')
    )

    image = models.ImageField(upload_to='blog images', verbose_name=_('Blog Image'))
    banner = models.ImageField(upload_to='blog banners', verbose_name=_('Blog Banner'))
    title = models.CharField(max_length=255, verbose_name=_('Blog Title'))
    little_about = models.TextField(verbose_name=_('Little About Blog'))
    full_about = RichTextUploadingField(verbose_name=_('Full About Blog'))
    blog_views = models.IntegerField(default=0, verbose_name=_('Blog Views'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Blog Created'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Blog Updated'))

    def __str__(self):
        return f'{self.title} | {self.created_at}'

    def get_comments(self):
        return self.comments.order_by('-pk')

    def get_related_blogs(self):
        return BlogModel.objects.filter(category_id=self.category_id).exclude(pk=self.pk)

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')


class BlogCommentModel(models.Model):
    blog = models.ForeignKey(
        BlogModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Blog')
    )
    name = models.CharField(max_length=30)
    email = models.EmailField()
    website = models.CharField(max_length=100)
    comment = models.TextField(verbose_name=_('Comment'))
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Submitted At'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
