from django import forms

from apps.schedules.models import Schedule
from apps.teachers.models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'subjects', 'date_of_birth', 'experiance', 'description', 'image']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'subjects': forms.Select(choices=Schedule.SUBJECT_CHOICES)
        }


