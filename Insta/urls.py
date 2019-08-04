from django.contrib import admin
from django.urls import include, path
from Insta.views import HelloWord, PostsView, PostDetailView

urlpatterns = [
    path('', HelloWord.as_view(), name = 'helloworld'),
    path('posts/', PostsView.as_view(), name = 'posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail')
]