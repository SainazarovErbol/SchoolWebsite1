from datetime import date
from django.db import models

from apps.users.models import CustomUser


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия'
    )
    subjects = models.CharField(
        max_length=100,
        verbose_name='Пердмет'
    )
    date_of_birth = models.DateField(
        verbose_name='Дата рождение'
        )
    experiance = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Опыт в годах:',
        )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='teacher_images/',
        null=True,
        blank=True,
        verbose_name='Фотографии'
    )

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )
