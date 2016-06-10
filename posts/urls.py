from django.conf.urls import include,url
from . import views



urlpatterns = [
    
    url(r'^$',views.posts_list, name="Home"),
    url(r'^create/$',views.posts_create, name="create"),
    url(r'^(?P<id>\d+)$',views.posts_detail, name="detail"),

    url(r'^update/$',views.posts_update, name="update"),
    url(r'^delete/$',views.posts_delete, name="delete"),
]
 