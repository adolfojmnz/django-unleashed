from django.http import Http404
from django.shortcuts import render
from .models import Tag, Startup, NewsLink

def homepage(request):
    template_name = 'organizer/tag_list.html'
    context       = {'tag_list': Tag.objects.all()}
    return render(request, template_name, context)

def tag_detail(request, slug):
    try:
        context = {'tag': Tag.objects.get(slug__iexact=slug)}
    except Tag.DoesNotExist:
        raise Http404(f'{slug} does not exist')
    template_name = 'organizer/tag_detail.html'
    return render(request, template_name, context)
