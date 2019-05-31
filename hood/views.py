from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Neighborhood,NeighborProfile,Business
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
  hoods=Neighborhood.objects.all()
  title = 'Our Hood'
  return render(request,'home.html',{"title":title,"hoods":hoods})

def hoods(request,id):
  hood = Neighborhood.objects.filter(id=neighborhood.id)
