from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Post


def home(request):

    return render(request, 'pages/index.html',)


@login_required
def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)

def about(request):
    return render(request, 'about/about.html')    


    
