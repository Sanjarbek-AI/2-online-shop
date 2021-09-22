from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('', include('home.urls', namespace='home')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('about/', include('about.urls', namespace='about')),
    path('order/', include('orders.urls', namespace='order')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('api/', include('api.urls', namespace='api')),
    path('product/', include('products.urls', namespace='product')),
    path('user/', include('users.urls', namespace='user')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
