from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Category Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Category Created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')


class ProductTagsModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Tag Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Tag Created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product Tag')
        verbose_name_plural = _('Product Tags')


class ProductSizeModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Tag Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Tag Created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product Size')
        verbose_name_plural = _('Product Sizes')


class ProductBrandModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Tag Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Tag Created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product Brand')
        verbose_name_plural = _('Product Brands')


class ProductColorModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Tag Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Tag Created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product Color')
        verbose_name_plural = _('Product Colors ')


class ProductModel(models.Model):
    categories = models.ManyToManyField(
        ProductCategoryModel,
        related_name='products',
        verbose_name=_('Categories')
    )
    tags = models.ManyToManyField(
        ProductTagsModel,
        related_name='products',
        verbose_name=_('Tags')
    )
    colors = models.ManyToManyField(
        ProductColorModel,
        related_name='products',
        verbose_name=_('Colors')
    )
    sizes = models.ManyToManyField(
        ProductSizeModel,
        related_name='products',
        verbose_name=_('Sizes')
    )
    brand = models.ForeignKey(
        ProductBrandModel,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name=_('Brand')
    )

    wishlist = models.ManyToManyField(
        UserModel,
        related_name='wishlist',
        verbose_name=_('Wishlist')
    )

    image_1 = models.ImageField(upload_to='products', verbose_name=_('Product Image 1'))
    image_2 = models.ImageField(upload_to='products', verbose_name=_('Product Image 2'))
    title = models.CharField(max_length=50, verbose_name=_('Product Title'))
    price = models.FloatField(verbose_name=_('Product Price'))
    little_about = models.TextField(verbose_name=_('Little About Product'))
    full_about = models.TextField(verbose_name=_('Full About Product'))
    in_stock = models.BooleanField(default=True, verbose_name=_('In Stock'))
    product_views = models.IntegerField(default=0, verbose_name=_('Product Views'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return f'{self.title} | {self.price}'

    def get_comments(self):
        return self.comments.order_by('-pk')

    def get_related_products(self):
        return ProductModel.objects.filter(brand_id=self.brand_id).exclude(pk=self.pk)

    @staticmethod
    def get_from_cart(request):
        cart = request.session.get('cart', [])
        return ProductModel.objects.filter(
            pk__in=cart
        )

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductImageModel(models.Model):
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Product')
    )
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return f'{self.product.title} | {self.product.price}'

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')


class ProductCommentModel(models.Model):
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Product')
    )
    comment = models.TextField(verbose_name=_('Comment'))
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Submitted At'))

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _('Product Comment')
        verbose_name_plural = _('Product Comments')
