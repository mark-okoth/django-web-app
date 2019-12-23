from django.urls import path
from . import views
from . views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


# all the urls concerning the blog page
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/post/<int:pk>/', PostDetailView.as_view(), name='post-details'),
    path('blog/post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('blog/post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('blog/post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='about')
]
