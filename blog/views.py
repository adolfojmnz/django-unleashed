from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm

from .utils import CreateObjectMixin, UpdateObjectMixin, DeleteObjectMixin


class GetPostObjectMixin:
    def get_post_object(self, year, month, slug):
        return (
            get_object_or_404(
                Post,
                pub_date__year  = year,
                pub_date__month = month,
                slug__iexact    = slug
            )
        )


class PostList(View):
    template_name = 'blog/post_list.html'

    def get(self, request, parent_template=None):
        context = {
            'post_list': Post.objects.all(),
            'parent_template': parent_template,
        }
        return render(request, self.template_name, context)


class PostDetail(View, GetPostObjectMixin):
    template_name = 'blog/post_detail.html'

    def get(self, request, year, month, slug, parent_template=None):
        context = {
            'post': self.get_post_object(year, month, slug),
            'parent_template': parent_template,
        }
        return render(request, self.template_name, context)


class PostCreate(View, CreateObjectMixin):
    form_class    = PostForm
    model         = Post
    model_name    = 'post'
    template_name = 'blog/post_form_create.html'


class PostUpdate(View, UpdateObjectMixin):
    form_class    = PostForm
    model         = Post
    model_name    = 'post'
    template_name = 'blog/post_form_update.html'


class PostDelete(View, DeleteObjectMixin):
    form_class    = PostForm
    model         = Post
    model_name    = 'post'
    template_name = 'blog/post_form_delete.html'
