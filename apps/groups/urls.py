from django.urls import path, include
from .views import *

urlpatterns = [
    path('group/api/', include('apps.groups.api.urls')),
    path('create_group/', create_group, name='create_group'),
    path('group/<int:group_id>/', group_detail, name='group_detail'),
    path('group/<int:group_id>/add_student/', add_student_to_group, name='add_student_to_group'),
    path('group/<int:group_id>/remove_student/<int:student_id>/', remove_student_from_group, name='remove_student_from_group'),
]
