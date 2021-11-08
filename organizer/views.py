from django.shortcuts import render
from .models import Tag, Startup, NewsLink

def homepage(request):
    template_name = 'organizer/tag_list.html'
    context = {'tag_list': Tag.objects.all()}
    return render(request, template_name, context)

def tag_detail(request):
    template_name = 'organizer/tag_detail.html'
    return render(request, template_name)

def startup_detail(request):
    template_name = 'organizer/startup_detail.html'
    return render(request, template_name)
