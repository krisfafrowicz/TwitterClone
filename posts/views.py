from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    #if method is POST
    if request.method == 'POST':
        form= PostForm(request.POST)
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
    output= 'POST ID is' +  str(post_id)
    return HttpResponse(output)


