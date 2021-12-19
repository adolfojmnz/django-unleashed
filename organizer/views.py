from django.shortcuts import render
from django.views.generic import View

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLinkForm

from .utils import CreateObjectMixin, UpdateObjectMixin, DeleteObjectMixin


def homepage(request):
    template_name = 'organizer/homepage.html'
    return render(request, template_name)


def tag_list(request):
    template_name = 'organizer/tag_list.html'
    context = {'tag_list': Tag.objects.all()}
    return render(request, template_name, context)


def tag_detail(request, slug):
    template_name = 'organizer/tag_detail.html'
    context = {'tag': get_object_or_404(Tag, slug__iexact=slug)}
    return render(request, template_name, context)


def startup_list(request):
    template_name = 'organizer/startup_list.html'
    context       = {'startup_list': Startup.objects.all()}
    return render(request, template_name, context)


def startup_detail(request, slug):
    template_name = 'organizer/startup_detail.html'
    context = {'startup': get_object_or_404(Startup, slug__iexact=slug)}
    return render(request, template_name, context)


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
