from django.urls import path

from .views import PostList, post_detail


urlpatterns = [
        path('post_list/', PostList.as_view(),
            {'parent_template': 'base.html'},
            name='post_list'
        ),

        path('<int:year>/<int:month>/<slug:slug>', post_detail,
            {'parent_template': 'base.html',
             'name': 'post_detail'}
        ),
]
