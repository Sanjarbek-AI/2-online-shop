"""
1. Task 
I have to create all apis for this website which is in here online shop.
And all of that have to be separated from each other, they should be easy to read and show

2. Task
I have to learn comment reply today in work or home.
"""
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from api.serializers import ProductModelSerializer, ProductCategoryModelSerializer
from products.models import ProductModel, ProductCategoryModel


class ProductListAPIView(ListAPIView):
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()


class ProductUpdateAPIView(UpdateAPIView, RetrieveAPIView):
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()


class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()


# Product Category API

class ProductCategoryListAPIView(ListAPIView):
    serializer_class = ProductCategoryModelSerializer
    queryset = ProductCategoryModel.objects.all()


class ProductCategoryUpdateAPIView(UpdateAPIView):
    serializer_class = ProductCategoryModelSerializer
    queryset = ProductCategoryModel.objects.all()


class ProductCategoryCreateAPIView(CreateAPIView):
    serializer_class = ProductCategoryModelSerializer
    queryset = ProductCategoryModel.objects.all()


class ProductCategoryDestroyAPIView(DestroyAPIView):
    serializer_class = ProductCategoryModelSerializer
    queryset = ProductCategoryModel.objects.all()
