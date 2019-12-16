from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def projects(request):
    return render (request, 'projects/projects.html')


@login_required
def profile(request):
    return render(request, 'profile/profile.html' )
