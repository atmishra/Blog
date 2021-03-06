from django.db import models
from django.conf import settings 
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from django.utils.safestring import mark_safe


from markdown_deux import markdown

''' def upload_location(instance,filename):
	return "%s/%s"%instance.id,filename
'''
class PostManager(models.Manager):
	def active(self,*args,**kargs):
		return super(PostManager,self).filter(draft=False).filter(publish__lte=timezone.now())

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	description = models.CharField(max_length=200, blank=True)
	slug = models.SlugField(unique = True)
	image = models.FileField(null=True,blank= True) 
	content = models.TextField()
	draft = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False, auto_now_add=False,default = timezone.now().date(),null=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	objects = PostManager()

	def __str__(self):
		return self.title; 

	def get_absolute_url(self):
		return reverse("posts:detail",kwargs={"slug":self.slug})
		# return "/posts/%s/"%(self.id)

	def get_marked_content(self):
		
		return mark_safe(markdown(self.content))

	class Meta:
		ordering = ["-timestamp","-updated"]

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug=new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s"%(slug,qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

'''For Adding Slug Field'''
def pre_save_post_receiver(signal,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_receiver,sender=Post)


	