
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
#

from apps.comments.forms import CommentForm
from apps.posts.api.serializers import *
from utils.permissions import AdminPermission
from rest_framework.permissions import IsAdminUser
#
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.teachers.models import Teacher
from apps.posts.mixins import FilteredPostListView

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
User = get_user_model()


from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm


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
    paginate_by = 6


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'post/post_detail.html'
#     form_class = CommentForm
#     success_url = '/'

def post_detail_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(request.path_info)# Перенаправляем на ту же страницу
    else:
        form = CommentForm()

    return render(request, 'post/post_detail.html', locals())


class PostCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_form.html'
    success_url = '/'
    extra = 3

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = inlineformset_factory(Post, PostImage, form=PostImagesForm, extra=self.extra)(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            data['formset'] = inlineformset_factory(Post, PostImage, form=PostImagesForm, extra=self.extra)()
        return data

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            print(formset.errors)

        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):

        data = super().get_context_data(**kwargs)

        if self.request.POST:
            data['formset'] = inlineformset_factory(Post, PostImage, form=PostImagesForm, extra=self.extra)(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            data['formset'] = inlineformset_factory(Post, PostImage, form=PostImagesForm, extra=self.extra)()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            form.instance.owner = self.request.user
            self.object = form.save()
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, RoleRequiredMixin, DeleteView):
    model = Post
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
