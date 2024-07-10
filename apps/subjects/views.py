from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Subject
from .forms import SubjectForm


@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subject_list.html', {'subjects': subjects})


@login_required
def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    return render(request, 'subjects/subject_detail.html', {'subject': subject})


@login_required
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subjects/subject_form.html', {'form': form})


@login_required
def subject_update(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'subjects/subject_form.html', {'form': form})


@login_required
def subject_delete(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'subjects/subject_confirm_delete.html', {'subject': subject})
