from django.contrib import admin
from apps.active_students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'grade')


admin.site.register(Student, StudentAdmin)
