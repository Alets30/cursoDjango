from django.shortcuts import render, redirect
from .models import Post,Job
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from . import forms
from django.forms import modelform_factory

# Create your views here.
def home(request):
    return render(request, 'posts/home.html',{
        "news": Post.objects.filter(points__gte=10).order_by('-points')
    })

def jobs(request):
    return render(request,'posts/jobs.html',{
        "jobs": Job.objects.all()
    })

addForm = modelform_factory(Post, exclude=['author','points','publicationDate'])
def add(request):
    form = addForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "website/add.html", {"form": form})

def sign_up(request):
    form = forms.SignUpForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        user = form.save()
        login(request,user)
        return redirect("home")
    else:
        print('no validO')
        return render(request,"registration/register.html",{"form":form})