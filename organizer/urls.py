from django.urls import path

from .views import (
        homepage,
		tag_list, tag_detail, tag_create, tag_update, tag_delete,
		startup_list, startup_detail,
)


urlpatterns = [
        # tags urls
        path('tag/', tag_list, name='tag_list'),
		path('tag/create/', tag_create, name='tag_create'),
        path('tag/<slug:slug>/', tag_detail, name='tag_detail'),
		path('tag/<slug:slug>/update/', tag_update, name='tag_update'),
		path('tag/<slug:slug>/delete/', tag_delete, name='tag_delete'),

        # startups urls
        path('startup/', startup_list, name='startup_list'),
        path('startup/<slug:slug>/', startup_detail, name='startup_detail'),
]
