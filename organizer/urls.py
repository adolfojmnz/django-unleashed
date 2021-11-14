from django.urls import path

from .views import (
        homepage, tag_list, tag_detail, startup_list, startup_detail
        )


urlpatterns = [
        # tags related urls
        path('tag/', tag_list, name='tag_list'),
        path('tag/<slug:slug>/', tag_detail, name='tag_detail'),

        # startups related urls
        path('startup/', startup_list, name='startup_list'),
        path('startup/<slug:slug>/', startup_detail, name='startup_detail'),
]

