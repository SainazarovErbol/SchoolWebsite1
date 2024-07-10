from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.db import IntegrityError
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
import requests
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
#
from rest_framework.permissions import IsAdminUser

from .forms import CustomAuthenticationForm, CustomUserUpdateForm
from .forms import CustomUserRegisterForm
from .models import CustomUser

from django.contrib.auth import login as auth_login
from django.views.generic import FormView


class SignUpView(UserPassesTestMixin, FormView):
    form_class = CustomUserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("У вас не достаточно прав доступа!")

    def form_valid(self, form):
        # Сохраняем пользователя
        user = form.save()

        # Логиним пользователя, чтобы сохранить сессию
        # auth_login(self.request, user)

        # Перенаправляем админа на текущую страницу или другую нужную страницу
        return redirect(self.success_url)


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect('/')


class CustomLoginView(LoginView):
    template_name = 'user/log_in.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        # This method is called when form is valid
        login(self.request, form.get_user())
        messages.success(self.request, 'You have successfully logged in.')
        return redirect('/')


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'user/user_profile.html'
    context_object_name = 'user'


class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    success_url = '../'
    template_name = 'user/profile_update.html'


def register(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../../')
    else:
        form = CustomUserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'user/register.html', locals())


