from django.http.response import HttpResponse

from .models import Tag, Startup, NewsLink


def homepage(request):
    li = ''

    for tag in Tag.objects.all():
        li += f'<li>{tag.__str__()}</li>\n'

    output = (
        '<!DOCTYPE HTML>' +
        '<html>' +
        ' <head>' +
        '   <Title>HomePage</title>' +
        '  </head>' +
        '  <body>' +
        '    <h3>Tags</h3>' +
        f'    {li}' +
        '  </body>' +
        '</hml>'
        )
    return HttpResponse(output)
