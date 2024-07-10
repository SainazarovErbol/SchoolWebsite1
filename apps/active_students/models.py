from django.db import models
from datetime import date


class Student(models.Model):
    GRADE_CHOICES = [
        (8, 'Grade 8'),
        (9, 'Grade 9'),
        (10, 'Grade 10'),
        (11, 'Grade 11'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    date_of_birth = models.DateField()
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    grade = models.IntegerField(choices=GRADE_CHOICES)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )
