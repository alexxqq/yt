from typing import Any
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView ,DetailView,CreateView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    videos = Videos.objects.all()

    context = {'videos':videos}
    return render(request,'yt/base.html',context)


def register_user(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'yt/login.html',context)

def login_user(request):
    form = LoginUserForm()

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    context = {'form':form}

    return render(request,'yt/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('home')

def account(request):
    profile = request.user.profile
    user_videos = profile.uploaded_videos.all()

    return render(request,'yt/account.html',{'user_videos': user_videos})

@login_required
def add_video(request):
    if request.method == 'POST':
        form = AddVideoForm(request.POST, request.FILES)

        if form.is_valid():
            if form.is_valid():
                video = form.save(commit=False)
                video.user = request.user
                video.save()
                return redirect('home')
    else:
        form = AddVideoForm()

    context = {'form': form}
    return render(request, 'yt/add_video.html', context)

def search(request):
    if request.method =='POST':
        searched = request.POST['searched']
        data = Videos.objects.filter(title=searched)
        if data:
            context = {'data':data,'match':True}
        else:

            context = {'data':data,'match':False}
        return render(request,'yt/search.html',context)
    else:
        return render(request,'yt/home.html')