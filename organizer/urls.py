from django.urls import path

from .views import (
		TagList, TagDetail, TagCreate, TagUpdate, TagDelete,
		StartupList, StartupDetail, StartupCreate, StartupUpdate, StartupDelete,
		NewsLinkList, NewsLinkCreate, NewsLinkDetail, NewsLinkUpdate, NewsLinkDelete,
)


urlpatterns = [
		# CBV for Tag model
		path('tag/', TagList.as_view(), name='tag_list'),
		path('tag/create/', TagCreate.as_view(), name='tag_create'),
		path('tag/<slug:slug>/', TagDetail.as_view(), name='tag_detail'),
		path('tag/<slug:slug>/update/', TagUpdate.as_view(), name='tag_update'),
		path('tag/<slug:slug>/delete/', TagDelete.as_view(), name='tag_delete'),

		# CBV for Startup class model
		path('startup/', StartupList.as_view(), name='startup_list'),
		path('startup/create/', StartupCreate.as_view(), name='startup_create'),
		path('startup/<slug:slug>/', StartupDetail.as_view(), name='startup_detail'),
		path('startup/<slug:slug>/update/', StartupUpdate.as_view(), name='startup_update'),
		path('startup/<slug:slug>/delete/', StartupDelete.as_view(), name='startup_delete'),

		# CBV for NewsLink model
		path('newslink/', NewsLinkList.as_view(), name='newslink_list'),
		path('newslink/create/', NewsLinkCreate.as_view(), name='newslink_create'),
		path('newslink/<slug:slug>/', NewsLinkDetail.as_view(), name='newslink_detail'),
		path('newslink/<slug:slug>/update/', NewsLinkUpdate.as_view(), name='newslink_update'),
		path('newslink/<slug:slug>/delete/', NewsLinkDelete.as_view(), name='newslink_delete'),
]
