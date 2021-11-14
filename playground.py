from django.template import Template, Context
from django.urls import reverse

from organizer.models import Tag


django_tag = Tag.objects.get(slug__iexact='django')
context = Context({'tag': django_tag.slug})
template = Template("{% url 'tag_detail' tag %}")
template.render(context)
