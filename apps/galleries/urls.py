from django.urls import path
from .views import *

urlpatterns = [
    # Gallery URLs
    path('gallery/', GalleryListView.as_view(), name='gallery_list'),
    path('gallery/<int:pk>/', GalleryDetailView.as_view(), name='gallery_detail'),
    path('gallery/create/', GalleryCreateView.as_view(), name='gallery_create'),
    path('gallery/<int:pk>/update/', GalleryUpdateView.as_view(), name='gallery_update'),
    path('gallery/<int:pk>/delete/', GalleryDeleteView.as_view(), name='gallery_delete'),
]
