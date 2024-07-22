from django.urls import path, include
from apps.posts.views import PostListView,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, AboutTemplateView, index_list


urlpatterns = [
    path('', index_list, name='index'),
    path('events/', PostListView.as_view(), name='post_list'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/api/', include('apps.posts.api.urls')),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]




