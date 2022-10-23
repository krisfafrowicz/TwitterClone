from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    #if method is POST
    if request.method == 'POST':
        form= PostForm(request.POST, request.FILES)
                #if form is valid
        if form.is_valid():
            #yes. save
            form.save()
                #redirect to home
            return HttpResponseRedirect('/')
                #no, show error
        else:
            return HttpResponseRedirect(form.erros.as_json())






    posts=Post.objects.all()[:20]

    return render(request, 'post.html',
            {'posts': posts})


def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')


def likecount(request, post_id):
    post = Post.objects.get(id = post_id)
    post.like +=1
    post.save()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    #if method is POST
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form= PostForm(request.POST, request.FILES, instance=post)
                #if form is valid
        if form.is_valid():
            #yes. save
            form.save()
                #redirect to home
            return HttpResponseRedirect('/')
                #no, show error
        else:
            return HttpResponseRedirect(form.erros.as_json())








    return render(request, 'edit.html',
            {'post': post})