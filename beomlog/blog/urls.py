from django.urls import path, include

from beomlog.blog.views import PostListView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
]