from django.views.generic import ListView, DetailView, CreateView

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


class PostCreateView(CreateView):
    model = Post
    fields = ['category', 'title', 'content']
    template_name = 'create.html'