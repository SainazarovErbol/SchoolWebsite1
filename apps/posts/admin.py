from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms
from apps.posts.models import Post, PostImage


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget(config_name='extends'))

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')


admin.site.register(Post, PostAdmin)

admin.site.register(PostImage)
