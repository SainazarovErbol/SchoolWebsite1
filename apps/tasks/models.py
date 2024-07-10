from django.db import models
from apps.groups.models import Group


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
