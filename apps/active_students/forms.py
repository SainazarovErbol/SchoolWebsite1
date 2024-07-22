from django import forms

from apps.active_students.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(format='%D/%M/%Y', attrs={'type': 'date'}),
            'phone_number': forms.NumberInput(attrs={'type': 'number'}),
            'email': forms.EmailInput(attrs={'type': 'email'})
        }

