from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCommentCreateView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', BlogCommentCreateView.as_view(), name='comment'),
]
