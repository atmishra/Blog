from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# Create your views here.
from .models import Post
from .forms import PostForm

def posts_list(request):

	allposts_list = Post.objects.active()
	if  request.user.is_staff or  request.user.is_superuser:
		allposts_list = Post.objects.all()
	# allposts_list = Contacts.objects.all()
	query = request.GET.get("q")
	if query:
		allposts_list = allposts_list.filter(
						Q(title__icontains=query) |
						Q(content__icontains=query)|
						Q(author__first_name__icontains=query)|
						Q(author__first_name__icontains=query)
						).distinct()
	paginator = Paginator(allposts_list, 5) 

	page = request.GET.get('page')
	try:
		page_posts = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		page_posts = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		page_posts = paginator.page(paginator.num_pages)
	context = {
		"page_posts": page_posts,
		"title": "Home",
		
		}	
	return render(request,"post_list.html",context)

def posts_create(request):
	print("hello")
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404 
	form = PostForm(request.POST or None, request.FILES or None )
	if form.is_valid():
		instance = form.save(commit=False)
		instance.author = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	

	context = {
		"form": form,
	}
	return render(request, "post_create.html", context)


def posts_detail(request,id = None, slug=None):

	instance = get_object_or_404(Post,slug = slug)
	if instance.draft or instance.publish > timezone.now().date():
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404 
	context = {
		"title" :instance.title,
		"instance": instance

	}
	return render(request,"post_detail.html",context) 




def posts_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404 
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_create.html", context)

	

def posts_delete(request,slug = None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404 
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("posts:Home")

def about(request):
	return render(request,"about.html")


def contact(request):
	return render(request,"contact.html")