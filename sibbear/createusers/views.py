from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from django.contrib.auth.models import User
from .models import City, Position


def index(request):
    if request.user.is_authenticated:
        return render(request, 'createusers/index.html')
    else:
        return HttpResponseRedirect("/admin/login/?next=/")

def mantis(request):
    return render(request, 'createusers/createmantis.html')
