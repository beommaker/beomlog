from django.conf.urls.static import static
from django.urls import path, include

from beomlog import settings
from beomlog.blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:post_pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:post_pk>/delete/', PostDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)