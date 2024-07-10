from django.urls import path
from .views import CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]
