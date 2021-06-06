from .models import BlogPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog_list_template.html"
    context_object_name = "blog_list"


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail_template.html"
    context_object_name = "blog_detail"


class CreateBlog(CreateView):
    model = BlogPost
    template_name = "create_blog.html"
    fields = "__all__"


class UpdateBlog(UpdateView):
    model = BlogPost
    template_name = "edit_blog.html"
    fields = ['title', 'body']


class DeleteBlog(DeleteView):
    model = BlogPost
    template_name = "delete_blog.html"
    success_url = reverse_lazy('blog_list')

