from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Post


class PostList(View):

    def get(self, request, parent_template=None):
        template_name = 'blog/post_list.html'
        context = {
                'post_list': Post.objects.all(),
                'parent_template': parent_template,
        }
        return render(request, template_name, context)


def post_detail(request, year, month, slug, parent_template=None):
    template_name = 'blog/post_detail.html'
    context = {
        'post': get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug,
        ),
        'parent_template': parent_template,
    }
    return render(request, template_name, context)

