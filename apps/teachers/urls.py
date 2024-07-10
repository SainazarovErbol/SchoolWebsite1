from django.urls import path

from apps.teachers.views import TeacherCreateView, TeacherListView, TeacherDetailView, TeacherUpdateView, TeacherDeleteView


urlpatterns = [
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('teachers/', TeacherListView.as_view(), name='list_teacher'),
    path('teachers/<int:pk>/detail/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete')
]

