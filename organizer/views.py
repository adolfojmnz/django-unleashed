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


class TagCreate(View, CreateObjectMixin):
    model = Tag
    form_class = TagForm
    template_name = 'organizer/tag_form_create.html'


class TagUpdate(View, UpdateObjectMixin):
    model = Tag
    form_class = TagForm
    context_name = 'tag'
    template_name = 'organizer/tag_form_update.html'


class TagDelete(View, DeleteObjectMixin):
    model = Tag
    form_class = TagForm
    context_name = 'tag'
    redirect_to  = 'tag_list'
    template_name = 'organizer/tag_form_delete.html'


class StartupList(View, ObjectListMixin):
    model = Startup
    context_name = 'startup_list'
    template_name = 'organizer/startup_list.html'


class StartupDetail(View, ObjectDetailMixin):
    model = Startup
    context_name = 'startup'
    template_name = 'organizer/startup_detail.html'


class StartupCreate(View, CreateObjectMixin):
    model = Startup
    form_class = StartupForm
    template_name = 'organizer/startup_form_create.html'


class StartupUpdate(View, UpdateObjectMixin):
    model = Startup
    form_class = StartupForm
    context_name = 'startup'
    template_name = 'organizer/startup_form_update.html'


class StartupDelete(View, DeleteObjectMixin):
    model = Startup
    form_class = StartupForm
    context_name = 'startup'
    redirect_to  = 'startup_list'
    template_name = 'organizer/startup_form_delete.html'


class NewsLinkCreate(View, CreateObjectMixin):
    model = NewsLink
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form_create.html'
