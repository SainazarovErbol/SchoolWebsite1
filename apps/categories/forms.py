from django import forms
from django.core.exceptions import ValidationError
from .models import Category


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Category.objects.filter(title=title).exists():
            raise ValidationError("Категории с таким названием уже существеут!")
        return title
