from django.db import models
from django.contrib.auth.models import User

from core.mixins import AutoDateMixin
from core.validators import validate_not_future_date


class UserProfile(AutoDateMixin):
    """Модель профиля пользователя"""
    
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER_CHOICES = {
        MALE: 'Мужской',
        FEMALE: 'Женский',
    }
    
    DIABETES_TYPE_CHOICES = {
        '1': '1',
        '2': '2',
    }
    
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Пользователь, к которому относится данный профиль',
    )
    patronymic_name = models.CharField(
        max_length=150,
        default='',
        verbose_name='Отчество',
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name='Пол',
    )
    birth_date = models.DateField(
        verbose_name='Дата рождения',
        validators=[validate_not_future_date],
    )
    diabetes_type = models.CharField(
        max_length=5,
        choices=DIABETES_TYPE_CHOICES,
        verbose_name='Тип диабета',
    )
    diagnosis_date = models.DateField(
        verbose_name='Дата постановки диагноза',
        validators=[validate_not_future_date],
        null=True,
        blank=True,
    )
    
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        ordering = ('updated_at',)
    
    def __str__(self):
        return f'Профиль пользователя {self.user}'
