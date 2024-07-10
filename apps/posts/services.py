import django_filters
from django.forms import TextInput

from .models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='contains',
        label='',  # Убирает метку
        widget=TextInput(attrs={'placeholder': 'Введите название'})
    )

    class Meta:
        model = Post
        fields = ['title']

