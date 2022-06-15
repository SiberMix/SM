from django.shortcuts import render
from django.http import HttpResponseRedirect, request
import subprocess
from .form.createmantis import СreateusersForm
import os
from django.contrib.auth.models import User
from .models import City, Position


def index(request):
    if request.user.is_authenticated:
        return render(request, 'createusers/index.html')
    else:
        return HttpResponseRedirect("/admin/login/?next=/")


def createusers(request):
    if request.method == 'POST':
        form = СreateusersForm(request.POST)
        if form.is_valid():
            ticket = request.POST['ticket']
            f = open("text.txt", "w")
            f.write(ticket)
            f.close()
            subprocess.call(['python', "./createusers/test.py", ticket])
    else:
        form = СreateusersForm()
    return render(request, 'createusers/createmantis.html', {'form': form})


def mantis(request):
    return render(request, 'createusers/createmantis.html')
