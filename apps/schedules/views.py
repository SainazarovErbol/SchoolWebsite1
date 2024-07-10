from django.shortcuts import render, get_object_or_404, redirect
from apps.grades.models import Grade
from .models import Schedule
from .forms import ScheduleForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def schedule_list(request):
    grades = Grade.objects.all()
    schedules = Schedule.objects.all().order_by('day_of_week', 'start_time')
    can_edit = request.user.is_superuser or request.user.has_perm('schedules.change_schedule')
    return render(request, 'schedules/schedule_list.html', {'grades': grades, 'schedules': schedules, 'can_edit': can_edit})


@login_required
def schedule_detail(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    schedules = grade.schedules.all().order_by('day_of_week', 'start_time')
    can_edit = request.user.is_superuser or request.user.has_perm('schedules.change_schedule')
    return render(request, 'schedules/schedule_detail.html', {'grade': grade, 'schedules': schedules, 'can_edit': can_edit})


@login_required
def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'schedules/schedule_form.html', {'form': form})


@login_required
def schedule_update(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule_detail', grade_id=schedule.grade.id)
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'schedules/schedule_form.html', {'form': form})


@login_required
def schedule_delete(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    grade_id = schedule.grade.id
    schedule.delete()
    return redirect('schedule_detail', grade_id=grade_id)


def get_days_for_grade(request, grade_id):
    days = Schedule.objects.filter(grade_id=grade_id).values_list('day_of_week', flat=True).distinct()
    return JsonResponse(list(days), safe=False)


def get_lessons_for_day(request, grade_id, day_of_week):
    schedules = Schedule.objects.filter(grade_id=grade_id, day_of_week=day_of_week).order_by('start_time')
    lessons = [{
        'start_time': schedule.start_time.strftime('%H:%M'),
        'end_time': schedule.end_time.strftime('%H:%M'),
        'subject': schedule.get_subject_display()
    } for schedule in schedules]
    return JsonResponse(lessons, safe=False)
