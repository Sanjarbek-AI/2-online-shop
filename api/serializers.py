from rest_framework import serializers

from products.models import ProductModel, ProductCategoryModel, ProductBrandModel, ProductColorModel, ProductTagsModel, \
    ProductSizeModel


class ProductCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        exclude = [
            'title_uz',
            'title_en',
            'title_ru',
        ]


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrandModel
        fields = '__all__'


class ColorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColorModel
        exclude = [
            'title_uz',
            'title_en',
            'title_ru',
        ]


class ProductTagsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTagsModel
        exclude = [
            'title_uz',
            'title_en',
            'title_ru',
        ]


class SizeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSizeModel
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    brand = BrandModelSerializer()
    categories = ProductCategoryModelSerializer(many=True)
    colors = ColorModelSerializer(many=True)
    sizes = SizeModelSerializer(many=True)
    tags = ProductTagsModelSerializer(many=True)

    class Meta:
        model = ProductModel
        exclude = [
            'title_uz',
            'title_en',
            'title_ru',
            'little_about_uz',
            'little_about_ru',
            'little_about_en',
            'full_about_uz',
            'full_about_ru',
            'full_about_en',
            'wishlist',
        ]
