from django.urls import path
from .views import CategoryListView, AddCategoryView, CategoryUpdateView, DeleteCategoryView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', AddCategoryView.as_view(), name='category_add'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/delete/<int:pk>/', DeleteCategoryView.as_view(), name='category_delete'),
]
