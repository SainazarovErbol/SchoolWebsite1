from django.urls import path
from .views import (
    schedule_list, schedule_detail, schedule_create,
    schedule_update, schedule_delete, get_days_for_grade,
    get_lessons_for_day
)

urlpatterns = [
    path('', schedule_list, name='schedule_list'),
    path('grade/<int:grade_id>/', schedule_detail, name='schedule_detail'),
    path('create/', schedule_create, name='schedule_create'),
    path('update/<int:schedule_id>/', schedule_update, name='schedule_update'),
    path('delete/<int:schedule_id>/', schedule_delete, name='schedule_delete'),
    path('grade/<int:grade_id>/days/', get_days_for_grade, name='get_days_for_grade'),
    path('grade/<int:grade_id>/days/<str:day_of_week>/', get_lessons_for_day, name='get_lessons_for_day'),
]

