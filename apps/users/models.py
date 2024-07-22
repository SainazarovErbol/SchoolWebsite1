from django.contrib.auth.models import AbstractUser, Permission, Group as DjangoGroup
from django.db import models

from apps.grades.models import Grade


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('staff', 'Персонал'),
        ('parent', 'Родитель'),
        ('teacher', 'Учитель'),
        ('student', 'Ученик'),
        ('content_maker', 'Контент_мейкер'),
    ]
    STUDENT_STATUS_CHOICES = [
        ('studying', 'Учится'),
        ('graduated_11', 'Окончил 11 класс'),
        ('graduated_9', 'Окончил 9 класс'),
        ('transferred', 'Переведен в другую школу'),
        ('expelled', 'Исключен'),
        ]
    TEACHER_STATUS_CHOICES = [
        ('active', 'Работает'),
        ('on_leave', 'В отпуске'),
        ('retired', 'На пенсии'),
        ('left', 'Уволился'),
    ]
    PARENT_STATUS_CHOICES = [
        ('active', 'Активный'),
        ('inactive', 'Неактивный'),
    ]
    student_status = models.CharField(max_length=20, choices=STUDENT_STATUS_CHOICES, blank=True, null=True)
    teacher_status = models.CharField(max_length=20, choices=TEACHER_STATUS_CHOICES, blank=True, null=True)
    parent_status = models.CharField(max_length=20, choices=PARENT_STATUS_CHOICES, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    enrollment_date = models.DateField(blank=True, null=True)

    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    parent_contact = models.CharField(max_length=100, blank=True, null=True)  # For students
    subject_specialization = models.CharField(max_length=100, blank=True, null=True)  # For teachers

    def __str__(self):
        return self.username

