from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from cerita_perjalanan.models import ceritaPerjalananItems
from cerita_perjalanan.forms import FormCerita
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@csrf_exempt
@login_required(login_url='/auth/login')
def submit_cerita(request):
    if request.method == 'POST':
        username = request.user.username
        form = FormCerita(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/story/')
    else:
        form = FormCerita()
    
    context = {
        'form':form,
        'cerita':ceritaPerjalananItems.objects.all(),
        'username':request.user.username
        }
    return render(request, 'cerita-perjalanan.html', context)

def get_cerita(request):
    form = FormCerita()
    username = request.user.username
    context = {
        'cerita':ceritaPerjalananItems.objects.all(),
        'username':username,
        'form':form
    }
    
    return render(request, 'cerita-perjalanan.html', context)

@csrf_exempt
@login_required(login_url='/auth/login')
def submit_cerita(request):
    if request.method == "POST":
        form = FormCerita(request.POST)
        form.instance.name = request.user.username
        if form.is_valid():
            form.save()
            response = HttpResponseRedirect("/story/")
            return response
    else:
        form = FormCerita()

    context = {'form':form}
    return render(request, 'cerita-perjalanan.html', context)

@csrf_exempt
@login_required(login_url='/auth/login')
def delete_cerita(request, id):
    task = ceritaPerjalananItems.objects.get(pk=id)
    task.delete()

    return HttpResponseRedirect("/story/")
        
