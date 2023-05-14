from django.shortcuts import render, redirect
from .models import Post,Job
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from . import forms
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def home(request):
    return render(request, 'posts/home.html',{
        "news": Post.objects.filter(points__gte=10).order_by('-points')
    })

def jobs(request):
    return render(request,'posts/jobs.html',{
        "jobs": Job.objects.all()
    })

AddForm = modelform_factory(Post,exclude=['publicationDate','points','author'])
@login_required(login_url='/accounts/login/')
def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user;
            obj.save()
            form = AddForm()
            return redirect('home')
            
    else:
        form = AddForm(request.POST)
        return render(request,"website/add.html",{'form':form})

def sign_up(request):
    form = forms.SignUpForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        user = form.save()
        print('valido')
        login(request,user)
        return redirect("home")
    else:
        print('no valido')
        return render(request,"registration/register.html",{"form":form})
    
@login_required(login_url='/accounts/login/')
def profile(request):
    form = forms.EditProfile(request.POST,instance=request.user)
    if form.is_valid():
        form.save()
        return redirect("profile")
    return render(request,"registration/profile.html",{"form":form,"name": User.get_full_name(request.user)})

@login_required(login_url='/accounts/login/')
def password(request):
    form = PasswordChangeForm(request.user,request.POST)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        return redirect("success")
    return render(request,"registration/password.html",{"form":form})

@login_required(login_url='/accounts/login/')
def password_success(request):
    return render(request,"registration/password_success.html")
