from django.urls import path

from .views import redirect_root


urlpatterns = [
        path('', redirect_root),
]

