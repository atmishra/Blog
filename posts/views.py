from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
from .forms import PostForm

def posts_list(request):

	allposts = Post.objects.all()

	context = {
		"object_list": allposts,
		"title": "list"
		}	
	return render(request,"index.html",context)

def posts_create(request):

	form = Form()
	context = {
		"form": form
	}
	return render(request,"post_create.html",context)

def posts_detail(request,id = None):

	instance = get_object_or_404(Post,id = id)
	context = {
		"title" :instance.title,
		"instance": instance

	}
	return render(request,"post_detail.html",context)



def posts_update(request):

	return HttpResponse("<h1> update </h1>")

def posts_delete(request):

	return HttpResponse("<h1> delete </h1>")
