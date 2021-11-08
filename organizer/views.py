from django.shortcuts import render
from .models import Tag, Startup, NewsLink

def homepage(request):
    template_name = 'organizer/homepage.html'
    return render(request, template_name)

def tag_list(request):
    template_name = 'organizer/tag_list.html'
    return render(request, template_name)

def tag_detail(request):
    template_name = 'organizer/tag_detail.html'
    return render(request, template_name)

def startup_detail(request):
    template_name = 'organizer/startup_detail.html'
    return render(request, template_name)
