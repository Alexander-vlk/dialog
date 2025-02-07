from django.db import models


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
