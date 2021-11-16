from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


def redirect_root(request):
    return redirect('post_list')

