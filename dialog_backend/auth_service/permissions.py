from rest_framework import permissions

from auth_service.constants import REFRESH_TOKEN_COOKIE_NAME


class HasNoRefreshToken(permissions.BasePermission):
    """Пользователь не имеет refresh-токена в cookie"""

    def has_permission(self, request, view):
        """Проверить наличие разрешения"""
        return not bool(request.COOKIES.get(REFRESH_TOKEN_COOKIE_NAME))


class HasRefreshToken(permissions.BasePermission):
    """Пользователь не имеет refresh-токена в cookie"""

    def has_permission(self, request, view):
        """Проверить наличие разрешения"""
        return bool(request.COOKIES.get(REFRESH_TOKEN_COOKIE_NAME))
