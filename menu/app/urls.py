from django.urls import path

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('<path:path>/', IndexView.as_view(), name='draw_menu'),
]
