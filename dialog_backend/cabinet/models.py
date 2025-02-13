from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

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

    FIRST_TYPE = '1'
    SECOND_TYPE = '2'
    MODY_TYPE = 'mody'
    GESTATIONAL = 'gestational'
    MANY_TYPES = 'many_types'
    DIABETES_TYPE_CHOICES = {
        FIRST_TYPE: '1-го типа',
        SECOND_TYPE: '2-го типа',
        MODY_TYPE: 'MODY-диабет',
        GESTATIONAL: 'Гестационный диабет',
        MANY_TYPES: 'Несколько типов диабета',
    }

    INSULIN_THERAPY = 'insulin_therapy'
    PREPARATIONS = 'preparations'
    TREATMENTS_TYPE_CHOICES = {
        INSULIN_THERAPY: 'Инсулинотерапия',
        PREPARATIONS: 'Препараты',
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
        max_length=20,
        choices=DIABETES_TYPE_CHOICES,
        verbose_name='Тип диабета',
    )
    diagnosis_date = models.DateField(
        verbose_name='Дата постановки диагноза',
        validators=[validate_not_future_date],
        null=True,
        blank=True,
    )

    treatment_type = models.CharField(
        verbose_name='Тип лечения',
        max_length=20,
        choices=TREATMENTS_TYPE_CHOICES,
        default='',
        blank=True,
    )

    phone_number = models.CharField(
        max_length=15,
        verbose_name='Номер телефона',
        default='',
        blank=True,
    )
    
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        ordering = ('updated_at',)
    
    def __str__(self):
        return f'Профиль пользователя {self.user}'


class Disease(AutoDateMixin):
    """Модель сопутствующих болезней"""
    
    users = models.ManyToManyField(
        to=User,
        verbose_name='Пользователи с заболеванием',
        related_name='diseases',
        blank=True,
        help_text='Указанные пользователи болеют этим заболеванием'
    )
    
    name = models.CharField(
        max_length=500,
        verbose_name='Название болезни',
    )
    
    class Meta:
        verbose_name = 'Заболевание'
        verbose_name_plural = 'Заболевания'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Allergy(AutoDateMixin):
    """Класс аллергии"""

    users = models.ManyToManyField(
        to=User,
        verbose_name='Пользователи',
        blank=True,
        related_name='allergies',
        help_text='Указанные пользователи имеют эту аллергию'
    )

    name = models.CharField(
        max_length=500,
        verbose_name='Название аллергии',
    )

    class Meta:
        verbose_name = 'Аллергия'
        verbose_name_plural = 'Аллергии'
        ordering = ['name']
