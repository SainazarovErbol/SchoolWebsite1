from django.db import models



class Grade(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name}"
