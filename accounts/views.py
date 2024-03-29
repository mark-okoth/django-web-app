from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from . import urls
from. import views


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f' Account created for{username}')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})
