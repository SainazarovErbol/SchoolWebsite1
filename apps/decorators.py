from django.http import HttpResponseForbidden
from functools import wraps
from apps.groups.models import Group


def group_member_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        group_id = kwargs.get('group_id')
        group = Group.objects.filter(id=group_id).first()

        if group:
            if request.user.role == 'teacher' and request.user == group.teacher:
                return view_func(request, *args, **kwargs)

            if request.user.role == 'student' and request.user in group.students.all():
                return view_func(request, *args, **kwargs)

        return HttpResponseForbidden("You do not have permission to access this group.")

    return _wrapped_view
