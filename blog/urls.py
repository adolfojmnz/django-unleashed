from django.urls import path

from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete


urlpatterns = [
	path('blog/', PostList.as_view(), name='post_list'),
	path('blog/create/', PostCreate.as_view(), name='post_create'),
    path('blog/<int:year>/<int:month>/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
	path('blog/<int:year>/<int:month>/<slug:slug>/update/', PostUpdate.as_view(), name='post_update'),
	path('blog/<int:year>/<int:month>/<slug:slug>/delete/', PostDelete.as_view(), name='post_delete'),
]
