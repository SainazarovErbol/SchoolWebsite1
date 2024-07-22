from django import forms
from .models import Post, PostImage
from django_ckeditor_5.widgets import CKEditor5Widget
from django.core.validators import FileExtensionValidator
from django.conf import settings


class PostImagesForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            })
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
        widgets = {
            'description': forms.Textarea(attrs={'id': 'id_description'}),
        }


class UploadFileForm(forms.Form):
    upload = forms.FileField(
        validators=[
            FileExtensionValidator(
                allowed_extensions=getattr(
                    settings,
                    "CKEDITOR_5_UPLOAD_FILE_TYPES",
                    ["jpeg", "png", "gif", "bmp", "webp", "tiff"]
                )
            ),
        ],
    )

