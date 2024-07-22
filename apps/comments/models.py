from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from apps.tasks.models import Task
from apps.users.models import CustomUser
from apps.posts.models import Post


class Comment(models.Model):
    text = CKEditor5Field(
        verbose_name='Комментарий',
        config_name='default',
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    user = models.ForeignKey(
        CustomUser,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.username


