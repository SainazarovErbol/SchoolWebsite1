from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', include('apps.users.urls')),
    path('', include('apps.posts.urls')),
    path('', include('apps.teachers.urls')),
    path('', include('apps.active_students.urls')),
    path('', include('apps.galleries.urls')),
    path('', include('apps.comments.urls')),
    path('schedules/', include('apps.schedules.urls')),
    path('subjects/', include('apps.subjects.urls')),
    path('grades/', include('apps.grades.urls')),
    path('groups/', include('apps.groups.urls')),
    path('tasks/', include('apps.tasks.urls')),
    path('token_create/', TokenObtainPairView.as_view()),
    path('token_refresh/', TokenRefreshView.as_view()),
]
