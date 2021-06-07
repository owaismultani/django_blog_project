from django.urls import path
from .views import BlogDetailView, BlogListView, CreateBlog, UpdateBlog, DeleteBlog

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_list"),
    path('<int:pk>/', BlogDetailView.as_view(), name="blog_detail"),
    path('new/', CreateBlog.as_view(), name="new_blog"),
    path('<int:pk>/edit/', UpdateBlog.as_view(), name='update_blog'),
    path('<int:pk>/delete/', DeleteBlog.as_view(), name='delete_blog')
]
