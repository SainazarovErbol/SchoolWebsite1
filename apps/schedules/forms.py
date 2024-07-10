from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['grade', 'subject', 'day_of_week', 'start_time', 'end_time']
        widgets = {
            'day_of_week': forms.Select(choices=Schedule.DAY_CHOICES),
            'subject': forms.Select(choices=Schedule.SUBJECT_CHOICES),
            'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
