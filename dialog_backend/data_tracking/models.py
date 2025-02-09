from django.db import models
from django.contrib.auth.models import User

from core.mixins import AutoDateMixin
from core.validators import validate_positive_float


class DailyLog(AutoDateMixin):
    """Модель ежедневных данных"""

    BAD = 'bad'
    NORMAL = 'normal'
    GREAT = 'great'
    TIREDNESS = 'tiredness'
    WEAKNESS = 'weakness'
    DROWSINESS = 'drowsiness'
    DIZZINESS = 'dizziness'
    NAUSEA = 'nausea'
    ANOTHER = 'another'
    GENERAL_HEALTH_CHOICES = {
        BAD: 'Плохое',
        NORMAL: 'Нормальное',
        GREAT: 'Отличное',
        TIREDNESS: 'Усталость',
        WEAKNESS: 'Слабость',
        DROWSINESS: 'Сонливость',
        DIZZINESS: 'Головокружение',
        NAUSEA: 'Тошнота',
        ANOTHER: 'Другое',
    }

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        verbose_name='Пользователь',
        related_name='daily_logs',
        null=True,
        blank=True,
    )

    calories_count = models.PositiveSmallIntegerField(
        verbose_name='Калории',
        help_text='Количество калорий за день',
    )

    proteins_count = models.PositiveSmallIntegerField(
        verbose_name='Белки',
        help_text='Количество белков за день (в граммах)',
    )

    fats_count = models.PositiveSmallIntegerField(
        verbose_name='Жиры',
        help_text='Количество жиров за день (в граммах)',
    )

    carbs_count = models.PositiveSmallIntegerField(
        verbose_name='Углеводы',
        help_text='Количество углеводов за день (в граммах)',
    )

    general_health = models.CharField(
        max_length=50,
        verbose_name='Общее самочувствие',
        choices=GENERAL_HEALTH_CHOICES,
        default=NORMAL,
    )

    physical_activity = models.CharField(
        max_length=2000,
        verbose_name='Физическая активность',
        help_text='Запишите сюда, какой физической активностью вы сегодня занимались',
        blank=True,
        default='',
    )

    additional_info = models.CharField(
        max_length=2000,
        verbose_name='Дополнительная информация',
        blank=True,
        default='',
    )

    class Meta:
        verbose_name = 'Дневной замер состояния'
        verbose_name_plural = 'Дневные замеры состояния'
        ordering = ['-updated_at']


class Glucose(AutoDateMixin):
    """Модель для уровня глюкозы"""

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    daily_log = models.ForeignKey(
        to=DailyLog,
        on_delete=models.CASCADE,
        verbose_name='Дневной замер состояния',
        related_name='glucoses',
    )

    level = models.FloatField(
        verbose_name='Уровень глюкозы',
        validators=[validate_positive_float],
    )

    class Meta:
        verbose_name = 'Уровень глюкозы'
        verbose_name_plural = 'Уровни глюкозы'


class Pressure(AutoDateMixin):
    """Модель для замеров давления"""

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    daily_log = models.ForeignKey(
        to=DailyLog,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Дневной замер состояния',
        related_name='pressures',
    )

    systolic = models.PositiveSmallIntegerField(
        verbose_name='Систолическое давление',
    )

    diastolic = models.PositiveSmallIntegerField(
        verbose_name='Диастолическое давление',
    )
