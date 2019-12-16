from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import urls
from. import views


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f' Account created for{username}')
            return redirect('login')
    else:
        form = UserCreationForm()        
    
    return render(request, 'accounts/register.html', {'form': form})

