from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . models import Post


def home(request):

    return render(request, 'pages/index.html',)


# @login_required
# def blog(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/blog.html', context)


def about(request):
    return render(request, 'about/about.html')


class PostListView( LoginRequiredMixin, ListView):
    model = Post   
    template_name = 'blog/blog.html'    
    context_object_name = 'posts'
    ordering =['-date_posted']


class PostDetailView(DetailView):
    model = Post   


class PostCreateView( LoginRequiredMixin, CreateView):
    model = Post 
    fields = ['title', 'content'] 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields = ['title', 'content'] 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 


    
           

