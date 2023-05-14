from django.shortcuts import render, redirect
from .models import Post,Job
from django.forms import modelform_factory

# Create your views here.
def home(request):
    return render(request, 'website/home.html',{
        "news": Post.objects.filter(points__gte=0).order_by('-points')
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