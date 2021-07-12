from rest_framework.permissions import BasePermission


class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 1)


class IsEditorUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 2)
