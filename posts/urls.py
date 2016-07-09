from django.conf.urls import include,url
from . import views



urlpatterns = [
    
    url(r'^$',views.posts_list, name="Home"),
    url(r'^create/$',views.posts_create, name="create"),
    url(r'^about/$',views.about, name="about"),
    url(r'^contact/$',views.contact, name="contact"),
    # url(r'^(?P<slug>.+)$',views.posts_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$',views.posts_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$',views.posts_delete, name="delete"),
    url(r'^(?P<slug>[\w-]+)$',views.posts_detail, name="detail"),
]
 