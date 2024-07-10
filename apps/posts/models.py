from django.db import models

from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = CKEditor5Field(
        verbose_name='Описание',
        config_name='default',
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.title}'


class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='PostImage'

    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='post_images/'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Изображение для {self.post.title}'
    
