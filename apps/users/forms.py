from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, TeacherRolePassword, ContentMakerRolePassword


class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )


class CustomUserRegisterForm(UserCreationForm):
    teacher_password = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.PasswordInput,
        help_text="Enter the teacher role password if you want to register as a teacher."
    )

    content_maker_password = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.PasswordInput,
        help_text='Введите пароль для Content Maker, если хотите зарегистрироваться в этой роли.'
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role', 'grade']

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get("role")
        teacher_password = cleaned_data.get("teacher_password")
        content_maker_password = cleaned_data.get('content_maker_password')

        if role == 'content_maker':
            if not content_maker_password:
                self.add_error('content_maker_password', 'Content Maker password is required.')
            else:
                try:
                    content_maker_role_password = ContentMakerRolePassword.objects.first()
                    if content_maker_role_password and content_maker_role_password.password != content_maker_password:
                        self.add_error('content_maker_password', 'Invalid Content Maker password.')
                except ContentMakerRolePassword.DoesNotExist:
                    self.add_error('content_maker_password', 'Content Maker password is not set by the admin.')

        if role == 'teacher':
            if not teacher_password:
                self.add_error('teacher_password', 'Teacher password is required.')
            else:
                try:
                    teacher_role_password = TeacherRolePassword.objects.first()
                    if teacher_role_password and teacher_role_password.password != teacher_password:
                        self.add_error('teacher_password', 'Invalid teacher password.')
                except TeacherRolePassword.DoesNotExist:
                    self.add_error('teacher_password', 'Teacher password is not set by the admin.')

        return cleaned_data


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
