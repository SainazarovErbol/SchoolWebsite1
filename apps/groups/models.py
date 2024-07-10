from django.db import models
from apps.users.models import CustomUser


class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='taught_groups')
    students = models.ManyToManyField(CustomUser, related_name='joined_groups')

    def __str__(self):
        return self.name

