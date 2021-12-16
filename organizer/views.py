from django.views.generic import View
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLink


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


class TagCreate(View):
    form_class = TagForm
    template_name = 'organizer/tag_form_create.html'

    def get(self, request):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
        else:
            context ={'form': form}
        return render(request, self.template_name, context)


class TagUpdate(View):
    form_class = TagForm
    template_name = 'organizer/tag_form_update.html'

    def get(self, request, slug):
        context = {
            'tag': Tag.objects.get(slug__iexact=slug),
            'form': self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        form = self.form_class(request.POST)
        if form.is_valid():
            updated_tag = form.save()
            return redirect(updated_tag)
        else:
            context = {
                'tag': Tag.objects.get(slug__iexact=slug),
                'form': form
            }
        return render(request, self.template_name, context)


class TagDelete(View):
    form_class = TagForm
    template_name = 'organizer/tag_form_delete.html'

    def get(self, request, slug):
        context = {
            'tag': Tag.objects.get(slug__iexact=slug),
            'form': self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        try:
            tag = Tag.objects.get(slug__iexact=slug)
        except Tag.DoesNotExist:
            raise Http404(f'Tag For {slug} Was Not Found!')
        if tag:
            tag.delete()
            return redirect(tag_list)


def startup_list(request):
    template_name = 'organizer/startup_list.html'
    context       = {'startup_list': Startup.objects.all()}
    return render(request, template_name, context)


def startup_detail(request, slug):
    template_name = 'organizer/startup_detail.html'
    context = {'startup': get_object_or_404(Startup, slug__iexact=slug)}
    return render(request, template_name, context)


class StartupCreate(View):
    form_class = StartupForm
    template_name = 'organizer/startup_form_create.html'

    def get(self, request):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_startup = form.save()
            return redirect(new_startup)
        else:
            context = {'form': form}
        return render(request, self.template_name, context)


class StartupUpdate(View):
    form_class = StartupForm
    template_name = 'organizer/startup_form_update.html'

    def get(self, request, slug):
        try:
            startup = Startup.objects.get(slug__iexact=slug)
        except Startup.DoesNotExist:
            return StartupCreate.get(request, slug)
        context = {
            'startup': startup,
            'form': self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        form = self.form_class(request.POST)
        if form.is_valid():
            updated_startup = form.save()
            return redirect(updated_startup)
        else:
            context = {
                'startup': Startup.objects.get(slug__iexact=slug),
                'form': form
            }
        return render(request, self.template_name, context)


class StartupDelete(View):
    form_class = StartupForm
    template_name = 'organizer/startup_form_delete.html'

    def get(self, request, slug):
        context = {
            'startup': Startup.objects.get(slug__iexact=slug),
            'form': self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.delete()
            return redirect(startup_list)
        else:
            context = {
                'startup': Startup.objects.get(slug__iexact=slug),
                'form': form
            }
        return render(request, self.template_name, context)
