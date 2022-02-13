from dataclasses import fields
from logging import PlaceHolder
from pyexpat import model
from tkinter import Widget
from tkinter.ttk import Style
from django import forms
from .models import  Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        # fields=["title","content","image","category"]
        exclude=['author','likes']
        
        
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control",'placeHolder':'Name'}),
            "content":forms.Textarea(attrs={"class":"form-control"}),
            "category":forms.Select(attrs={"class":"form-control"}),
        }
        
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']