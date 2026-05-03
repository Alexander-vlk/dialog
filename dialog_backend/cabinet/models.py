from django.db import models

from common_utils.mixins import AutoDateMixin


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
