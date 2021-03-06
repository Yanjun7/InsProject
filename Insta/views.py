from django.views.generic import TemplateView, ListView, DetailView
from Insta.models import Post
# HelloWord is a Template-view

class HelloWord(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
