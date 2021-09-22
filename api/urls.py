from django.urls import path

from api.views import ProductListAPIView, ProductCreateAPIView, ProductUpdateAPIView, ProductDestroyAPIView, \
    ProductRetrieveAPIView

app_name = 'api'


urlpatterns = [
    path('products/list', ProductListAPIView.as_view(), name='products-list'),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='products-detail'),
    path('products/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='products-delete'),
    path('products/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='products-update'),
    path('products/create/', ProductCreateAPIView.as_view(), name='products-create'),
]

