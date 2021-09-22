from django.urls import path

from products.views import ProductListView, ProductDetailView, WishListView, add_wishlist, add_to_cart, CartListView

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('wishlist/<int:pk>/', add_wishlist, name='add-wishlist'),
    path('cart/<int:pk>/', add_to_cart, name='add-to-cart'),
]
