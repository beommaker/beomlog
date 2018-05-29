from django.views.generic import ListView, DetailView, CreateView

from beomlog.blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['category', 'title', 'content']
    template_name = 'create.html'