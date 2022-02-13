from multiprocessing.sharedctypes import Value
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
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
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=3000)
    image=models.ImageField(blank=True, upload_to='post_images')
    author=models.ForeignKey(User ,on_delete=models.CASCADE)
    category=models.ForeignKey(Category ,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name='blogpost_like', blank=True)
    
  
    def __str__(self):
        return self.title
    @property
    def number_of_likes(self):
        return self.likes.all().count()
    
# LIKE_CHOICES=(
#     ("Like","Like"),
#     ("Unlike","Unlike")
# )    

# class Like(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)   
#     post=models.ForeignKey(Post,on_delete=models.CASCADE)   
#     value=models.CharField(choices=LIKE_CHOICES, default="Like",max_length=10)
    
#     def __str__(self):
#         return str(self.post)
    
# class Comment(models.Model):
#     time_stamp=models.DateTimeField(auto_now_add=True, blank=False)
#     content=models.TextField(max_length=300)
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     post=models.ForeignKey(Post,on_delete=models.CASCADE)
    
 

class Comment(models.Model): 
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE) 
    body = models.TextField(blank=True) 
    created = models.DateTimeField(auto_now_add=True,blank=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 

    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post) 
    
# @receiver (pre_save, sender=Post)
# def pre_save_receiver(sender, instance, *args, **kwargs):
#    if not instance.slug:
#        instance.slug = unique_slug_generator (instance)