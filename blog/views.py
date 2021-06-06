from .models import BlogPost
from django.views.generic import ListView, DetailView


# Create your views here.


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog_list_template.html"
    context_object_name = "blog_list"


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail_template.html"
    context_object_name = "blog_detail"
