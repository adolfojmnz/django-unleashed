from django.urls import path

from .views import (
	PostList,
	PostArchiveYearIndex, PostArchiveYear,
	PostCreate, PostDetail, PostUpdate, PostDelete,
)


urlpatterns = [
	path('blog/archives/', PostArchiveYearIndex.as_view(), name='post_archives_year_index'),
	path('blog/archives/<int:year>/', PostArchiveYear.as_view(), name='post_archive_year'),

	path('blog/', PostList.as_view(), name='post_list'),
	path('blog/create/', PostCreate.as_view(), name='post_create'),
	path('blog/<int:year>/<int:month>/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
	path('blog/<int:year>/<int:month>/<slug:slug>/update/', PostUpdate.as_view(), name='post_update'),
	path('blog/<int:year>/<int:month>/<slug:slug>/delete/', PostDelete.as_view(), name='post_delete'),
]
