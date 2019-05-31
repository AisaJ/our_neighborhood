from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
# Create your views here.

def home(request):
  title = 'Our Hood'
  return render(request,'home.html',{"title":title})
