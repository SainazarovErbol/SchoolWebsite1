from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name='Название')

    def __str__(self):
        return f'{self.title}'
