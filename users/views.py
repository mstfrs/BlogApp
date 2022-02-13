from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages




# Create your views here.




def home_view(request):
    return render(request, 'users/home.html')




def profile(request):
#     user=Profile.objects.get()
#     context={
#       "user":user
#    }
        
    return render(request,'registration/profile.html')

def register(request):
    
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()          
            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            
            user=authenticate(username=username,password=password)
            
            login(request,user)
            return redirect('post')
    else:          
     
        form=UserCreationForm()
    context={
        'form':form
    }
    return render(request, 'registration/register.html',context)


@login_required
def profile(request):
    return render(request, 'registration/profile.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'registration/profile.html', context)