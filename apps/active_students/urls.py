from django.urls import path
from .views import StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('active_students/', StudentListView.as_view(), name='student_list'),
    path('active_students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('active_students/create/', StudentCreateView.as_view(), name='student_create'),
    path('active_students/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_update'),
    path('active_students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]
