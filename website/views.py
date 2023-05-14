from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post, Job
# Create your views here.
def welcome(request):
    return render(request,"website/welcome.html",{
        "info": "Curso introductorio Django",
        "suma": 5+2
    })

def page_not_found(request,exception):
    return render(request,'website/404.html',status=404)

def upvote(request):
    id = (request.body).decode('UTF-8')
    post = Post.objects.get(pk=id)
    post.points = post.points + 1
    post.save()
    return redirect('home')