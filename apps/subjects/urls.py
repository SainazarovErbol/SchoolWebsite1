from django.urls import path
from .views import subject_list, subject_detail, subject_create, subject_update, subject_delete

urlpatterns = [
    path('', subject_list, name='subject_list'),
    path('<int:subject_id>/', subject_detail, name='subject_detail'),
    path('create/', subject_create, name='subject_create'),
    path('update/<int:subject_id>/', subject_update, name='subject_update'),
    path('delete/<int:subject_id>/', subject_delete, name='subject_delete'),
]
