from django.urls import path
from .views import homepage, tag_detail


urlpatterns = [
        path('', homepage, name='homepage'),
        path('tag/<slug:slug>/', tag_detail, name='tag_detail'),
]

