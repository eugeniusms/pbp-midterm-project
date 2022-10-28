from django.shortcuts import render
from daftar_event.models import Event
from daftar_event.forms import event_form
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def daftar_event(request) :
  daftar_event = Event.objects.all()
  user_loggedin = request.user.username
  user_admin = "aulia"
  
  context = {
    'daftar_event' : daftar_event,
    'user_loggedin' : user_loggedin,
    'user_admin' : user_admin,
  }
  return render(request,"daftar_event.html",context)

@login_required(login_url='/auth/login')
@csrf_exempt
def tambah_event(request) :
  form = event_form(request.POST or None)
  context = {
    'forms' : form
  }
  return render(request,'tambah_event.html',context)

def show_json(request) :
  data = Event.objects.all()
  return HttpResponse(serializers.serialize("json",data),content_type="application/json")

@login_required(login_url='/auth/login')
@csrf_exempt
def delete_all(request,id):
  if(request.user.username == "aulia") :
    event = Event.objects.all()
    event.delete()
  return redirect('daftar_event:daftar_event')

@login_required(login_url='/auth/login')
@csrf_exempt
def delete_event(request,id):
  if(request.user.username == "aulia") :
    event = Event.objects.get(id=id)
    event.delete()
  return redirect('daftar_event:daftar_event')
  
def lihat_event(request, id):
  event = Event.objects.get(pk=id)
  context = {
    'nama': event.nama,
    'lokasi': event.lokasi,
    'jenis': event.jenis,
    'deskripsi' : event.deskripsi,
  }
  return render(request, 'event.html', context)

@login_required(login_url='/auth/login')
@csrf_exempt
def add_json(request):
  if request.method=='POST':
    nama = request.POST.get('nama')
    print(nama, 1212312)
    lokasi = request.POST.get('lokasi')
    jenis = request.POST.get('jenis')
    deskripsi = request.POST.get('deskripsi')
    Event.objects.create(nama=nama, lokasi=lokasi, jenis = jenis, deskripsi=deskripsi)
    return JsonResponse({"Sukses": "Data masuk"},status=200)

def category_event(request,cat):
  data = Event.objects.filter(jenis=cat)
  if cat == "All":
    data = Event.objects.all()
  return HttpResponse(serializers.serialize("json",data),content_type="application/json")