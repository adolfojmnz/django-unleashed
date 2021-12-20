from django.views.generic import View
from django.shortcuts import render, get_object_or_404

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLinkForm

from .utils import (
	ObjectListMixin, ObjectDetailMixin,
	CreateObjectMixin, UpdateObjectMixin, DeleteObjectMixin,
)


class TagList(View, ObjectListMixin):
	model = Tag
	context_name = 'tag_list'
	template_name = 'organizer/tag_list.html'


class TagDetail(View, ObjectDetailMixin):
	model = Tag
	context_name = 'tag'
	template_name = 'organizer/tag_detail.html'


class StartupList(View, ObjectListMixin):
	model = Startup
	context_name = 'startup_list'
	template_name = 'organizer/startup_list.html'


class StartupDetail(View, ObjectDetailMixin):
	model = Startup
	context_name = 'startup'
	template_name = 'organizer/startup_detail.html'


class TagCreate(View, CreateObjectMixin):
    form_class = TagForm
    template_name = 'organizer/tag_form_create.html'
    model_name = 'tag'


class TagUpdate(View, UpdateObjectMixin):
    form_class = TagForm
    template_name = 'organizer/tag_form_update.html'
    model = Tag
    model_name = 'tag'


class TagDelete(View, DeleteObjectMixin):
    form_class = TagForm
    template_name = 'organizer/tag_form_delete.html'
    model = Tag
    model_name = 'tag'


class StartupCreate(View, CreateObjectMixin):
    form_class = StartupForm
    template_name = 'organizer/startup_form_create.html'
    model_name = 'startup'


class StartupUpdate(View, UpdateObjectMixin):
    form_class = StartupForm
    template_name = 'organizer/startup_form_update.html'
    model = Startup
    model_name = 'startup'


class StartupDelete(View, DeleteObjectMixin):
    form_class = StartupForm
    template_name = 'organizer/startup_form_delete.html'
    model = Startup
    model_name = 'startup'


class NewsLinkCreate(View, CreateObjectMixin):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form_create.html'
    model_name = 'newslink'
