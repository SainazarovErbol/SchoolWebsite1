from django.db import models
from apps.grades.models import Grade


class Schedule(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
        ('Saturday', 'Суббота'),
        ('Sunday', 'Воскресенье')
    ]

    SUBJECT_CHOICES = [
        ('Math', 'Математика'),
        ('Physics', 'Физика'),
        ('Chemistry', 'Химия'),
        ('Biology', 'Биология'),
        ('History', 'История'),
        ('Geography', 'География'),
        ('English', 'Английский язык'),
        ('Physical Education', 'Физическая культура'),
        ('Music', 'Музыка'),
        ('Art', 'ИЗО')
        # Add other subjects as needed
    ]

    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='schedules')
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    day_of_week = models.CharField(max_length=20, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.grade.name} - {self.get_day_of_week_display()} - {self.get_subject_display()}"

    def get_day_of_week_display(self):
        return dict(self.DAY_CHOICES).get(self.day_of_week)

    def get_subject_display(self):
        return dict(self.SUBJECT_CHOICES).get(self.subject)

