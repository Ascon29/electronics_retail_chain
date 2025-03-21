from rest_framework import permissions


class UserIsActive(permissions.BasePermission):
    """Проверка, является ли пользователь активным"""

    def has_permission(self, request, view):
        return request.user.is_active
