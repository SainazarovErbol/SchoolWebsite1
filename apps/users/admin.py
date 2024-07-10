from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TeacherRolePassword, ContentMakerRolePassword
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(TeacherRolePassword)
class TeacherRolePasswordAdmin(admin.ModelAdmin):
    pass


@admin.register(ContentMakerRolePassword)
class ContentMakerRolePasswordAdmin(admin.ModelAdmin):
    pass
