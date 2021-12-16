from django.urls import path

from .views import (
		homepage,
		TagCreate, TagUpdate, TagDelete,
		tag_list, tag_detail,
		StartupCreate, StartupUpdate, StartupDelete,
		startup_list, startup_detail,
)


urlpatterns = [
		# CBV for Tag model
		path('tag/create/', TagCreate.as_view(), name='tag_create'),
		path('tag/<slug:slug>/update/', TagUpdate.as_view(), name='tag_update'),
		path('tag/<slug:slug>/delete/', TagDelete.as_view(), name='tag_delete'),

		# CBV for Startup class model
        path('startup/create/', StartupCreate.as_view(), name='startup_create'),
        path('startup/<slug:slug>/update/', StartupUpdate.as_view(), name='startup_update'),
        path('startup/<slug:slug>/delete/', StartupDelete.as_view(), name='startup_delete'),

        # Function Views for Tag model
        path('tag/', tag_list, name='tag_list'),
        path('tag/<slug:slug>/', tag_detail, name='tag_detail'),

        # Function Views for Startup model
        path('startup/', startup_list, name='startup_list'),
        path('startup/<slug:slug>/', startup_detail, name='startup_detail'),
]
