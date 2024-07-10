from rest_framework.permissions import IsAdminUser


class AdminPermission(IsAdminUser):
    def has_permission(self, request, view):

        if request.user and request.user.is_staff:
            return True

        if view.action == 'list':
            return True
        return False
