from django.db import models
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.request import Request


class AutoDateMixin(models.Model):
    """Миксин для добавления даты создания и даты обновления"""

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )

    class Meta:
        abstract = True


class ReadOnlyOrStaffMixin:
    """Миксин для разграничения доступов к разным actions в ViewSet"""

    request: Request

    SAFE_ACTIONS = ['list', 'retrieve']

    def has_permissions(self):
        """Проверка наличия доступов по разным actions"""
        if self.request.method in self.SAFE_ACTIONS:
            return [AllowAny()]

        return [IsAdminUser()]
