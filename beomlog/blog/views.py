from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from beomlog.blog.models import Post, Category


class PostListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category=category_id)
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    fields = ['category', 'title', 'content', 'image']
    template_name = 'create.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['category', 'title', 'content', 'image']
    template_name = '_update.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = '_delete.html'
    pk_url_kwarg = 'post_pk'