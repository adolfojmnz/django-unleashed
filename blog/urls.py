from django.urls import path

from .views import PostList, PostDetail


urlpatterns = [
        path('blog/', PostList.as_view(), {'parent_template': 'base.html'},
            name = 'post_list'
		),

        path('blog/<int:year>/<int:month>/<slug:slug>', PostDetail.as_view(), {'parent_template': 'base.html'},
            name = 'post_detail'
        ),
]
