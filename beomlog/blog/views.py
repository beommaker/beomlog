from django.shortcuts import render, get_object_or_404

from beomlog.blog.models import Post


def home(request):
    template_name = 'home.html'
    posts = Post.objects.all()
    context_data = {'object_list': posts}

    return render(request, template_name, context_data)


def detail(request, post_id):
    template_name = 'detail.html'
    post = get_object_or_404(Post, id=post_id)
    context_data = {'object': post}
    return render(request, template_name, context_data)
