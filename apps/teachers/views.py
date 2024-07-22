from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from apps.teachers.models import Teacher
from .forms import TeacherForm


# CRUD Techers

class TeacherCreateView(UserPassesTestMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/teacher_form.html'
    success_url = reverse_lazy('list_teacher')

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("У вас не достаточно прав доступа!")


class TeacherListView(ListView):
    model = Teacher
    template_name = 'trainers.html'
    context_object_name = 'teachers'


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher/detail.html'
    context_object_name = 'teacher'


class TeacherUpdateView(UserPassesTestMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/teacher_form.html'

    def get_success_url(self):
        return reverse_lazy('teacher_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("У вас не достаточно прав доступа!")


class TeacherDeleteView(UserPassesTestMixin, DeleteView):
    model = Teacher
    template_name = 'teacher/delete_confirm.html'
    success_url = reverse_lazy('list_teacher')

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("У вас не достаточно прав доступа!")
