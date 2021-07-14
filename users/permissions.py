from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        if not (request.method in SAFE_METHODS) and (isinstance(request.user, AnonymousUser)):
            return False
        if (request.method in SAFE_METHODS) and (isinstance(request.user, AnonymousUser)):
            return True
        else:
            return bool(request.user and request.user.role == 1)


class IsEditorUser(BasePermission):
    def has_permission(self, request, view):

        if not (request.method in SAFE_METHODS) and (isinstance(request.user, AnonymousUser)):
            return False
        if (request.method in SAFE_METHODS) and (isinstance(request.user, AnonymousUser)):
            return True
        else:
            return bool(request.user and request.user.role == 2)
