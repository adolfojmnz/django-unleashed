from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLink


def homepage(request):
    template_name = 'organizer/homepage.html'
    return render(request, template_name)

	
def tag_list(request):
    template_name = 'organizer/tag_list.html'
    context       = {'tag_list': Tag.objects.all()}
    return render(request, template_name, context)


def tag_detail(request, slug):
	if slug == 'create':
		return tag_create(request)
	else:
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


# helper functions
def tag_create(request):
	if request.method == 'POST':
		form = TagForm(request.POST)
		if form.is_valid():
			new_tag = form.save()
			return redirect(new_tag)
		else:
			context = {'form': form}
	elif request.method == 'GET':
		context = {'form': TagForm()}

	template_name = 'organizer/tag_form_create.html'
	return render(request, template_name, context)


def tag_update(request, slug):
	if request.method == 'POST':
		form = TagForm(request.POST)
		if form.is_valid():
			updated_tag = form.save()
			return redirect(updated_tag)
		else:
			context = {'slug': slug, 'form': form}
	elif request.method == 'GET':
		form = TagForm(instance=Tag.objects.get(slug__iexact=slug))
		context = {'slug': slug, 'form': form}

	template_name = 'organizer/tag_form_update.html'
	return render(request, template_name, context)


def tag_delete(request, slug):
	if request.method == 'POST':
		tag = Tag.objects.get(slug__iexact=slug)
		if tag:
			tag.delete()
			return redirect(tag_list)
		else:
			raise Tag.DoesNotExist
	elif request.method == 'GET':
		template_name = 'organizer/tag_form_delete.html'
		context = {'tag': Tag.objects.get(slug__iexact=slug)}
		return render(request, template_name, context)
