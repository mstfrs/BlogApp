
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import pre_save

from blogApp.util import unique_slug_generator
# from .models import Category


# Create your models here.

class Category(models.Model):
    CATEGORY_CHOICES=[
        ( 'FrontEnd','FE'),
        ('BackEnd','BE' ),
        ('FullStack','FS' ),
    ]
    name=models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    CATEGORY_CHOICES=[
        ( 'FrontEnd','FrontEnd'),
        ('BackEnd','BackEnd' ),
        ('FullStack','FullStack' ),
    ]
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=3000)
    image=models.ImageField(blank=True, upload_to='post_images')
    author=models.ForeignKey(User ,on_delete=models.CASCADE)
    category=models.CharField(max_length=100, choices=CATEGORY_CHOICES,default="FS")
    likes=models.ManyToManyField(User,related_name='blogpost_like', blank=True)
    
  
    def __str__(self):
        return self.title
    @property
    def number_of_likes(self):
        return self.likes.all().count()
    

 

class Comment(models.Model): 
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE) 
    body = models.TextField(blank=True) 
    created = models.DateTimeField(auto_now_add=True , blank=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 

    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post) 
    
