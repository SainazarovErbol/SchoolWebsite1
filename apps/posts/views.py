from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import MultipleObjectMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#
from django.template.loader import render_to_string
from django_ckeditor_5.forms import UploadFileForm
from django_ckeditor_5.views import image_verify, NoImageException, handle_uploaded_file
from django.utils.translation import gettext_lazy as _

from apps.comments.forms import CommentForm
from apps.posts.api.serializers import *
from utils.permissions import AdminPermission
from rest_framework.permissions import IsAdminUser
#
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.teachers.models import Teacher
from apps.posts.mixins import FilteredPostListView, PaginationMixin

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.forms import inlineformset_factory
from apps.posts.models import Post, PostImage
from apps.posts.forms import PostForm, PostImagesForm
from django.contrib.auth.mixins import LoginRequiredMixin

from ..categories.models import Category

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm, PostImagesForm
User = get_user_model()





class RoleRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.role == 'content_maker'


# class PostCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'post/post_form.html'
#     success_url = reverse_lazy('post_list')





def index_list(request):
    all_events = Post.objects.all()
    return render(request, 'index.html', locals())




class PostListView(FilteredPostListView, ListView):
    model = Post
    template_name = 'events.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category', None)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'post/post_detail.html'
#     form_class = CommentForm
#     success_url = '/'



class PostDetailView(PaginationMixin, DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        # Pagination for images
        image_page_data = self.paginate_queryset(post.PostImages.all(), 'image_page')
        context.update({
            'image_page_obj': image_page_data['page_obj'],
            'image_paginator': image_page_data['paginator'],
            'image_is_paginated': image_page_data['is_paginated'],
        })

        # Pagination for comments
        comment_page_data = self.paginate_queryset(post.comments.all(), 'comment_page')
        context.update({
            'comment_page_obj': comment_page_data['page_obj'],
            'comment_paginator': comment_page_data['paginator'],
            'comment_is_paginated': comment_page_data['is_paginated'],
        })

        # Comment form
        if self.request.method == 'POST':
            form = CommentForm(self.request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = self.request.user
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()

        context['form'] = form
        return context




class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        PostImageFormSet = inlineformset_factory(Post, PostImage, form=PostImagesForm, extra=3)
        if self.request.POST:
            data['formset'] = PostImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['formset'] = PostImageFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        return super().form_valid(form)



class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/update_post.html'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        PostImageFormSet = inlineformset_factory(Post, PostImage, form=PostImagesForm, extra=3)
        if self.request.POST:
            data['formset'] = PostImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['formset'] = PostImageFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        return self.form_invalid(form)


class PostDeleteView(LoginRequiredMixin, RoleRequiredMixin, DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')


class AboutTemplateView(ListView):
    template_name = 'about.html'
    model = Teacher

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['teachers_count'] = Teacher.objects.all().count()
        return context


# Serializer class
class PostAPIViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        elif self.action == 'retrieve':
            return PostSerializer
        elif self.action == 'list':
            return PostListSerializer
        elif self.action == 'destroy':
            return PostDeleteSerializer
        return PostSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AdminPermission]
        return super().get_permissions()


class PostImageViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return PostImageCreateSerializer
        elif self.action == 'list':
            return PostImageListSerializer
        elif self.action == 'retrieve':
            return PostImageSerializer
        elif self.action == 'update':
            return PostImageUpdateSerializer
        elif self.action == 'partial_update':
            return PostImageUpdateSerializer
        elif self.action == 'destroy':
            return PostImageDeleteSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AdminPermission]
        return super().get_permissions()


@csrf_exempt
def custom_upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        allow_all_file_types = getattr(settings, "CKEDITOR_5_ALLOW_ALL_FILE_TYPES", False)

        if not allow_all_file_types:
            try:
                image_verify(request.FILES["upload"])
            except NoImageException as ex:
                return JsonResponse({"error": {"message": f"{ex}"}}, status=400)

        if form.is_valid():
            url = handle_uploaded_file(request.FILES["upload"])
            return JsonResponse({"url": url})

    raise Http404(_("Page not found."))