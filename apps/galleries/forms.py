from django import forms

from apps.galleries.models import Gallery, Image, Video


class ImageForm(forms.ModelForm):
    class Meta:
        models = Image
        fields = ('image', 'caption')
        widgets = {'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
        })}


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('title', 'description')


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video_file','caption')
        widgets = {'video_file': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
        })}

