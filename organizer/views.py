from django.shorcuts import render

from .models import Tag, Startup, NewsLink


def homepage(request):
    output = ''
    template_name = 'templates/organizer/tag_detail.html'
    return render(output, template_name)
