from django.urls import reverse_lazy
from django.views.generic import (
    View, ListView, DetailView, CreateView, UpdateView, DeleteView,
)

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLinkForm


# Tag views
class TagList(ListView):
    model = Tag
    context_object_name = 'tag_list'
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
    template_name = 'organizer/tag_form_delete.html'
    success_url = reverse_lazy('tag_list')


# Startup views
class StartupList(ListView):
    model = Startup
    context_object_name = 'startup_list'
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
    template_name = 'organizer/startup_form_delete.html'
    success_url = reverse_lazy('startup_list')


# NewsLink views
class NewsLinkList(ListView):
	model = NewsLink
	context_object_name = 'newslink_list'
	template_name = 'organizer/newslink_list.html'


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
    template_name = 'organizer/newslink_form_delete.html'
    success_url = reverse_lazy('newslink_list')
