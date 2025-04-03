from django.db import models
from django.contrib.auth.models import User

from core.mixins import AutoDateMixin
from core.validators import validate_not_future_date
from constants import DIABETES_TYPE_CHOICES, GENDER_CHOICES, TREATMENTS_TYPE_CHOICES


class UserProfile(AutoDateMixin):
    """Модель профиля пользователя"""

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Пользователь, к которому относится данный профиль',
    )

    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name='Фото',
        default='images/stub.png',
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
        blank=True,
        default='',
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

    @property
    def fio(self):
        return f'{self.user.last_name} {self.user.first_name} {self.patronymic_name}'


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
