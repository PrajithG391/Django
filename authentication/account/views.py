from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,"Registration successful.")
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request,'account/register.html',{'form':form})
    
def profile(request):
    return render(request,'account/profile.html')

    