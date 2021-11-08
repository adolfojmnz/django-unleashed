from django.urls import path
from .views import homepage, tag_list, tag_detail, startup_detail


urlpatterns = [
        path('', homepage, name='homepage'),
        path('tag_list/', tag_list, name='tag_list'),
        path('tag_detail/', tag_detail, name='tag_detail'),
        path('startup_detail/', startup_detail, name='startup_detail'),
]
