from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.decorators import group_member_required

from apps.comments.models import Comment
from apps.comments.forms import CommentForm
from .models import Task
from .forms import TaskForm
from ..groups.models import Group


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user.role != 'teacher' or request.user != task.group.teacher:
        return HttpResponseForbidden("You do not have permission to edit this task.")

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', locals())


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user.role != 'teacher' or request.user != task.group.teacher:
        return HttpResponseForbidden("You do not have permission to delete this task.")

    if request.method == 'POST':
        task.delete()
        return redirect('group_detail', group_id=task.group.id)

    return render(request, 'tasks/delete_task.html', locals())


@login_required
def create_task(request):
    if request.user.role != 'teacher':
        return redirect('../../')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            group = form.cleaned_data['group']

            if request.user != group.teacher:
                return redirect('../../')

            task.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm()

    return render(request, 'tasks/create_task.html',  locals())


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    return render(request, 'tasks/task_detail.html', locals())
