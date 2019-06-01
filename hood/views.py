from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Neighborhood,NeighborProfile,Business
from django.contrib.auth.decorators import login_required
from .forms import NewHoodForm,NewProfileForm,NewBusinessForm
# Create your views here.

def home(request):
  hoods=Neighborhood.objects.all()
  title = 'Our Hood'
  return render(request,'home.html',{"title":title,"hoods":hoods})

@login_required(login_url='/accounts/login')
def hoods(request,id):
  hood = Neighborhood.objects.filter(id=neighborhood.id)

  return render(request,'hood.html',{"hood":hood})

@login_required(login_url='/accounts/login')
def new_hood(request):
  current_user = request.user 
  if request.method == 'POST':
    form = NewHoodForm(request.POST,request.FILES)
    if form.is_valid():
      hood = form.save(commit=False)
      hood.user = current_user
      hood.save()
    return redirect('home')
  else:
    form=NewHoodForm()
    return render(request,'new_hood.html',{"form":form})

@login_required(login_url='/accounts/login')
def new_neighbour(request):
  current_user =  request.user 
  if request.method == 'POST':
    form = NewProfileForm(request.POST,request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user =  current_user
      prof_pic=form.cleaned_data['prof_pic']
      name=form.cleaned_data['name']
      email= form.cleaned_data['email']
      NeighborProfile.objects.filter(user=current_user).update(prof_pic=prof_pic,name=name,email=email)
      NeighborProfile.save()
       
    return redirect('newNeighbour')
  else:
    form=NewProfileForm()
    return render(request,'new_neighbor.html',{"form":form})

