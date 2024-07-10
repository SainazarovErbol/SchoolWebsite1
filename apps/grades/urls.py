from django.urls import path
from .views import grade_list, grade_detail, grade_create, grade_update, grade_delete

urlpatterns = [
    path('', grade_list, name='grade_list'),
    path('<int:grade_id>/', grade_detail, name='grade_detail'),
    path('create/', grade_create, name='grade_create'),
    path('update/<int:grade_id>/', grade_update, name='grade_update'),
    path('delete/<int:grade_id>/', grade_delete, name='grade_delete'),
]
