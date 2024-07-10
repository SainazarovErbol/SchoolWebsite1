from django import forms

from apps.posts.models import Post, PostImage
from django_ckeditor_5.widgets import CKEditor5Widget


class PostImagesForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('image',)
        widgets = {'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
        })}


class PostForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget(config_name='default'))

    class Meta:
        model = Post
        fields = ['title', 'description']
