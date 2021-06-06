from django.views.generic import TemplateView


class homeView(TemplateView):
    template_name = "home.html"