from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from apps.grades.models import Grade


class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )


class CustomUserRegisterForm(UserCreationForm):
    grade = forms.ModelChoiceField(
        queryset=Grade.objects.all(),
        required=False,
        widget=forms.Select,
        help_text="Select the grade if you are registering as a student."
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role', 'grade']

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get("role")
        grade = cleaned_data.get("grade")

        if role == 'student' and not grade:
            self.add_error('grade', 'Grade is required for students.')

        return cleaned_data


class CustomUserTeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserStudentUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'photo',
            'parent_contact',
            'student_status',
            'address',
            'grade',
            'date_of_birth',

        ]

