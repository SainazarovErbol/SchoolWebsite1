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
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
#

from .forms import CustomAuthenticationForm, CustomUserStudentUpdateForm
from .forms import CustomUserRegisterForm
from .models import CustomUser

from django.views.generic.edit import FormView
from django.http import HttpResponseForbidden


class SignUpView(UserPassesTestMixin, FormView):
    form_class = CustomUserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('register')

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас недостаточно прав доступа!")

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Пользователь {username} успешно зарегистрирован!')
        return redirect(reverse('register'))


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
        messages.success(self.request, 'Вы успешно вошли в аккаунт!')
        return redirect('index')


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'user/user_profile.html'
    context_object_name = 'user'


class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserStudentUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'user/profile_update.html'

    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        else:
            return False

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас недостаточно прав доступа!")



