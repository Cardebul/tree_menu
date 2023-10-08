from django.views.generic import TemplateView
from .models import Menu


class IndexView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = {}
        path = self.kwargs.get("path")
        if path:
            path = path.split("/")
            if path:
                context["name"] = path[0]
                context["item"] = path[-1]
                return context
        context["menus"] = Menu.objects.all()
        return context
