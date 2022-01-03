from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm

from .utils import (
	ObjectListMixin, ObjectDetailMixin,
	CreateObjectMixin, UpdateObjectMixin, DeleteObjectMixin,
)


class PostList(View, ObjectListMixin):
	model = Post
	paginate_by = 1
	context_name = 'post_list'
	template_name = 'blog/post_list.html'


class PostDetail(View, ObjectDetailMixin):
	model = Post
	context_name = 'post'
	template_name = 'blog/post_detail.html'


class PostCreate(View, CreateObjectMixin):
    form_class    = PostForm
    model         = Post
    template_name = 'blog/post_form_create.html'


class PostUpdate(View, UpdateObjectMixin):
    form_class    = PostForm
    model         = Post
    context_name  = 'post'
    template_name = 'blog/post_form_update.html'


class PostDelete(View, DeleteObjectMixin):
    form_class    = PostForm
    model         = Post
    context_name  = 'post'
    redirect_to   = 'post_list'
    template_name = 'blog/post_form_delete.html'
