from django.urls import reverse
from multiprocessing import context
from unicodedata import category
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import  PostForm, CommentForm
from django.shortcuts import redirect, render
from .models import Category, Post
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
# Create your views here.

def post_list(request):
   print(User.username)
   posts=Post.objects.all()   
   context={
      "posts":posts
      
   }
   return render(request, 'blog/post_list.html',context)

def BlogPostLike(request, id):
    post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        print("number_of_likes")

    return HttpResponseRedirect(reverse('post_details', args=[str(id)]))
 
 

 

def post_create(request):
   form=PostForm(request.POST or None)
   
   if request.method=="POST":
      form=PostForm(request.POST, request.FILES)
      if form.is_valid() :
         new_creator=form.save(commit=False)
         new_creator.author =request.user         
         new_creator.save()
         form.save_m2m()
         
         return redirect("post_list")
         
   context={
      "form":form
   }
   return render(request,"blog/post_create.html",context)





def post_details(request, id):
    template_name = 'blog/post_details.html'
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.name= request.user
            
            # new_comment.email=request.email
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
    
def post_update(request,id):
   post=Post.objects.get(id=id)
   form=PostForm(instance=post)
   if request.method=="POST":
      form=PostForm(request.POST, request.FILES, instance=post )
      if form.is_valid():
         form.save()
         return redirect("post_list")
   context={
      "form":form
   }
   return render(request,"blog/post_update.html", context)   

def post_delete(request,id):
   post=Post.objects.get(id=id)
   if request.method=="POST":
      post.delete()
      return redirect("post_list")
   context={
      "post":post
   }
   return render(request,"blog/post_delete.html",context) 
    

    
    
