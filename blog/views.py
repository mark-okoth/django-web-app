from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'pages/index.html')
    
@login_required
def blog(request):
    return render(request, 'blog/blog.html' )

def about(request):
    return render(request, 'about/about.html')    


    
