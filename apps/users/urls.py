from django.urls import path
#
from apps.users.views import *
#
urlpatterns = [
    path('account/register/', SignUpView.as_view(), name='register'),
    path('account/login/', CustomLoginView.as_view(), name='login'),
    path('account/logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', UserUpdateView.as_view(), name='profile_update')
]
