from django.urls import path,include
from .views import home_view, profile, register
from blog.views import post_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', post_list,name="post"),
    path('register/', register ,name="register"),
    path('profile/', profile ,name="profile"),
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)