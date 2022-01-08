from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic import (
	CreateView, DetailView, UpdateView, DeleteView,
	View, ListView, YearArchiveView,
)

from .models import Post
from .forms import PostForm

from .utils import YearArchiveIndexView


class PostList(ListView):
	model = Post
	context_object_name = 'post_list'
	template_name = 'blog/post_list.html'


class PostDetail(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'


class PostCreate(CreateView):
    form_class    = PostForm
    model         = Post
    template_name = 'blog/post_form_create.html'


class PostUpdate(UpdateView):
    form_class    = PostForm
    model         = Post
    template_name = 'blog/post_form_update.html'


class PostDelete(DeleteView):
    model         = Post
    success_url   = reverse_lazy('post_list')
    template_name = 'blog/post_form_delete.html'


class PostArchiveYearIndex(YearArchiveIndexView):
	model = Post
	context_object_name = 'archive_index'
	template_name = 'blog/post_archive_year_index.html'


class PostArchiveYear(YearArchiveView):
	model = Post
	date_field = 'pub_date'
	make_object_list = True
	context_object_name = 'archives'
	template_name = 'blog/post_archive_year.html'
