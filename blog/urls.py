

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import  post_create, post_list, post_details, post_update,post_delete,BlogPostLike

urlpatterns = [
    path('details/<int:id>', post_details, name='post_details'),
    path('blogpost-like/<int:id>', BlogPostLike, name="blogpost_like"),
    path('create',post_create, name="post_create"),
    path('list/',post_list , name="post_list"),
    path('update/<int:id>', post_update ,name="post_update"),
    path('delete/<int:id>', post_delete ,name="post_delete"),
    
     
    
  
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
