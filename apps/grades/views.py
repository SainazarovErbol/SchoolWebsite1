from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Grade
from .forms import GradeForm

@login_required
def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grades/grade_list.html', {'grades': grades})

@login_required
def grade_detail(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    return render(request, 'grades/grade_detail.html', {'grade': grade})

@login_required
def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'grades/grade_form.html', {'form': form})

@login_required
def grade_update(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'grades/grade_form.html', {'form': form})

@login_required
def grade_delete(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')
    return render(request, 'grades/grade_confirm_delete.html', {'grade': grade})
