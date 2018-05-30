from django.urls import path, include

from beomlog.blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:post_pk>/update/', PostUpdateView.as_view(), name='update'),
]