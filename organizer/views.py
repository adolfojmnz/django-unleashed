from django.views.generic import View
from django.shortcuts import render, get_object_or_404

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLinkForm

from .utils import (
	ListView, CreateView, DetailView, UpdateView, DeleteView,
)


class TagList(ListView):
    model = Tag
    context_name = 'tag_list'
    template_name = 'organizer/tag_list.html'


class TagDetail(DetailView):
    model = Tag
    template_name = 'organizer/tag_detail.html'


class TagCreate(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'organizer/tag_form_create.html'


class TagUpdate(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'organizer/tag_form_update.html'


class TagDelete(DeleteView):
    model = Tag
    form_class = TagForm
    redirect_to  = 'tag_list'
    template_name = 'organizer/tag_form_delete.html'


class StartupList(ListView):
	model = Startup
	paginate_by = 1
	initial_page_number = 1
	context_name = 'startup_list'
	template_name = 'organizer/startup_list.html'


class StartupDetail(DetailView):
    model = Startup
    template_name = 'organizer/startup_detail.html'


class StartupCreate(CreateView):
    model = Startup
    form_class = StartupForm
    template_name = 'organizer/startup_form_create.html'


class StartupUpdate(UpdateView):
    model = Startup
    form_class = StartupForm
    template_name = 'organizer/startup_form_update.html'


class StartupDelete(DeleteView):
    model = Startup
    form_class = StartupForm
    redirect_to  = 'startup_list'
    template_name = 'organizer/startup_form_delete.html'


class NewsLinkCreate(CreateView):
    model = NewsLink
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form_create.html'


class NewsLinkDetail(DetailView):
    model = NewsLink
    template_name = 'organizer/newslink_detail.html'


class NewsLinkUpdate(UpdateView):
    model = NewsLink
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form_update.html'


class NewsLinkDelete(DeleteView):
    model = NewsLink
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form_delete.html'
