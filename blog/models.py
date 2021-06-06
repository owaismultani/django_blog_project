from django.db import models
from django.urls import reverse

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title[0:100]

    def get_absolute_url(self):
        return reverse('blog_list')
