from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Group
from .forms import GroupForm
from apps.decorators import group_member_required
from apps.users.models import CustomUser

from rest_framework import viewsets
from .api.serializers import GroupCreateUpdateSerializer, GroupDetailSerializers, GroupDeleteSerializer, GroupListSerializer



@login_required
def create_group(request):
    if request.user.role != 'teacher':
        return redirect('home')

    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.teacher = request.user
            group.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm()

    return render(request, 'groups/create_group.html', locals())


@login_required
@group_member_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.user.role == 'teacher' and request.user != group.teacher:
        return HttpResponseForbidden("You do not have permission to access this group.")

    if request.user.role == 'student' and request.user not in group.students.all():
        return HttpResponseForbidden("You do not have permission to access this group.")

    return render(request, 'groups/group_detail.html', locals())


@login_required
@group_member_required
def add_student_to_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.user.role != 'teacher' or request.user != group.teacher:
        return redirect('index')

    if request.method == 'POST':
        student_username = request.POST.get('student_username')
        student = get_object_or_404(CustomUser, username=student_username)

        if student.role == 'teacher':
            return redirect('group_detail', group_id=group.id)

        group.students.add(student)
        return redirect('group_detail', group_id=group.id)

    return render(request, 'groups/add_student_to_group.html', locals())

@login_required
@group_member_required
def remove_student_from_group(request, group_id, student_id):
    group = get_object_or_404(Group, id=group_id)
    student = get_object_or_404(CustomUser, id=student_id)

    if request.user.role != 'teacher' or request.user != group.teacher:
        return redirect('home')

    group.students.remove(student)
    return redirect('group_detail', group_id=group.id)


class GroupAPIVewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return GroupCreateUpdateSerializer
        elif self.action == 'destroy':
            return GroupDeleteSerializer
        elif self.action == 'list':
            return GroupListSerializer
        elif self.action == 'retrieve':
            return GroupDetailSerializers
        return GroupDetailSerializers
