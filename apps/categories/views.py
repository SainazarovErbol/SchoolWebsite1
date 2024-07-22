from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from .forms import CategoryCreateForm
from .models import Category


class CategoryListView(UserPassesTestMixin, ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.role == 'content_maker'


class AddCategoryView(UserPassesTestMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_superuser or self.request.user.role == 'content_maker')

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас недостаточно прав доступа!")


class CategoryUpdateView(UserPassesTestMixin, UpdateView):
    model = Category
    fields = ['title']
    template_name = 'categories/category_list.html'
    success_url = reverse_lazy('category_list')

    def test_func(self):
        try:
            return self.request.user.is_authenticated and (self.request.user.is_superuser or self.request.user.role == 'content_maker')
        except AttributeError:
            return HttpResponseForbidden("У вас недостаточно прав доступа!")

class DeleteCategoryView(UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'categories/category_list.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.role == 'content_maker'

    def get(self, request, pk, *args, **kwargs):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect(reverse('category_list'))
