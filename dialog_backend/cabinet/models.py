from django.db import models

from auth_service.models import AppUser
from common_utils.mixins import AutoDateMixin
from common_utils.validators import validate_length


class DiabetesType(AutoDateMixin):
    """Модель типов диабета"""

    name = models.CharField(max_length=100, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип диабета'
        verbose_name_plural = 'Справочник типов диабета'
        ordering = ['name']

    def __str__(self):
        return self.name


class TreatmentType(AutoDateMixin):
    """Модель типов лечения"""

    name = models.CharField(max_length=100, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип лечения'
        verbose_name_plural = 'Справочник типов лечения'
        ordering = ['name']

    def __str__(self):
        return self.name


class Disease(AutoDateMixin):
    """Справочник сопутствующих заболеваний"""

    name = models.CharField(
        max_length=500,
        verbose_name='Название',
    )

    class Meta:
        verbose_name = 'Сопутствующее заболевание'
        verbose_name_plural = 'Справочник сопутствующих заболеваний'
        ordering = ['name']

    def __str__(self):
        return self.name
