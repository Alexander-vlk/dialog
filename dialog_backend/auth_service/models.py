from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from common_utils.mixins import AutoDateMixin
from common_utils.validators import validate_not_future_date
from constants import GENDER_CHOICES, UNDEFINED


class Town(AutoDateMixin):
    """Справочник городов"""

    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    timedelta = models.IntegerField(verbose_name='Отклонение по часам')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Справочник городов'
        ordering = ['name']

    def __str__(self):
        return self.name


class AppUser(AbstractUser, AutoDateMixin):
    """Модель пользователя"""

    town = models.ForeignKey(
        Town,
        verbose_name='Город',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
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
        blank=True,
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name='Пол',
        default=UNDEFINED,
    )
    height = models.SmallIntegerField(
        verbose_name='Рост',
        null=True,
        blank=True,
        validators=[validators.MinValueValidator(1)],
    )
    birth_date = models.DateField(
        verbose_name='Дата рождения',
        validators=[validate_not_future_date],
        null=True,
        blank=True,
    )
    diabetes_type = models.ForeignKey(
        'cabinet.DiabetesType',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Тип диабета',
        related_name='users',
    )
    diagnosis_date = models.DateField(
        verbose_name='Дата постановки диагноза',
        validators=[validate_not_future_date],
        null=True,
        blank=True,
    )
    treatment_type = models.ForeignKey(
        'cabinet.TreatmentType',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Тип лечения',
        related_name='users',
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Номер телефона',
        default='',
        blank=True,
    )
    moods = models.ManyToManyField(
        'data_tracking.Mood',
        verbose_name='Связанные настроения',
        through='data_tracking.MoodAppUser',
        related_name='users_with_mood',
        blank=True,
    )
    healths = models.ManyToManyField(
        'data_tracking.Health',
        verbose_name='Связанные самочувствия',
        through='data_tracking.HealthAppUser',
        related_name='users_with_health',
        blank=True,
    )
    diseases = models.ManyToManyField(
        'cabinet.Disease',
        verbose_name='Сопутствующие заболевания',
        related_name='users_with_disease',
        blank=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('updated_at',)

    def __str__(self):
        return f'{self.username}'

    @property
    def fio(self):
        return f'{self.last_name} {self.first_name} {self.patronymic_name}'
