from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import BlogPost
from django.urls import reverse


class TestPage(TestCase):
    username = "test_user"
    email = "test@gmail.com"
    password = "test_password"
    title = "Test Post"
    body = "This is test blog"

    def setUp(self):
        self.user = get_user_model().objects.create(
            username=self.username,
            email=self.email,
            password=self.password
        )
        self.blog = BlogPost.objects.create(
            title=self.title,
            author=self.user,
            body=self.body
        )

    def test_model_string(self):
        self.assertEqual(str(self.blog), self.blog.title)

    def test_blog_list(self):
        self.assertEqual(self.blog.title, self.title)
        self.assertEqual(str(self.blog.author), self.username)
        self.assertEqual(self.blog.body, self.body)

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.title)
        self.assertTemplateUsed(response, 'blog_list_template.html')

    def test_blog_detail_view(self):
        response = self.client.get('/blogs/1')
        no_response = self.client.get('/blogs/1000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.body)
        self.assertTemplateUsed(response, 'blog_detail_template.html')

    def test_create_blog(self):
        response = self.client.post(reverse('new_blog'), {
            "title": self.title,
            "author": self.username,
            "body": self.body
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.title)

    def test_update_blog(self):
        response = self.client.post(reverse("update_blog", args='1'),{
            "title": self.title + " (edited)"
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.title + " (edited)")

    def test_delete_blog(self):
        response = self.client.get(reverse("delete_blog", args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.title)






