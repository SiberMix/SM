from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from .form.createmantis import СreateusersForm


def index(request):
    if request.user.is_authenticated:
        return render(request, 'createusers/index.html')
    else:
        return HttpResponseRedirect("/admin/login/?next=/")

def createusers(request):
    if request.method == 'POST':
        pass
    else:
        form = СreateusersForm()
    return render(request, 'createusers/createmantis.html', {'form': form})


