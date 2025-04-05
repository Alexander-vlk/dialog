from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from core.mixins import AutoDateMixin
from core.validators import validate_positive_float


class MonthlyLog(AutoDateMixin, models.Model):
    """Модель ежемесячного отчета"""

    MONTH_CHOICES = {
        '1': 'Январь',
        '2': 'Февраль',
        '3': 'Март',
        '4': 'Апрель',
        '5': 'Май',
        '6': 'Июнь',
        '7': 'Июль',
        '8': 'Август',
        '9': 'Сентябрь',
        '10': 'Октябрь',
        '11': 'Ноябрь',
        '12': 'Декабрь',
    }

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Пользователь',
        related_name='monthly_log',
    )

    hemoglobin = models.PositiveSmallIntegerField(
        verbose_name='Гликированный гемоглобин',
        null=True,
        blank=True,
    )

    cholesterol = models.FloatField(
        validators=[validate_positive_float],
        verbose_name='Уровень холестерина',
        null=True,
        blank=True,
    )

    lipid_profile = models.FloatField(
        validators=[validate_positive_float],
        verbose_name='Липидный профиль',
        null=True,
        blank=True,
    )

    microalbuminuria = models.PositiveSmallIntegerField(
        verbose_name='Микроальбуминурия',
        null=True,
        blank=True,
    )

    month = models.CharField(
        choices=MONTH_CHOICES,
        max_length=10,
        verbose_name='Месяц',
    )

    class Meta:
        verbose_name = 'Месячный замер состояния'
        verbose_name_plural = 'Месячные замеры состояния'


class WeeklyLog(AutoDateMixin):
    """Модель еженедельного отчета"""

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Пользователь',
    )

    monthly_log = models.ForeignKey(
        to=MonthlyLog,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Ежемесячный отчет',
    )

    weight = models.PositiveSmallIntegerField(
        verbose_name='Вес',
    )

    bmi = models.PositiveSmallIntegerField(
        verbose_name='Индекс массы тела',
    )

    ketones = models.FloatField(
        validators=[validate_positive_float],
        verbose_name='Кетоны',
    )

    week_start = models.DateField(
        default=timezone.now,
        verbose_name='Дата начала недели',
    )

    week_end = models.DateField(
        default=timezone.now,
        verbose_name='Дата окончания недели',
    )

    class Meta:
        verbose_name = 'Еженедельный отчет'
        verbose_name_plural = 'Еженедельные отчеты'


class DailyLog(AutoDateMixin):
    """Модель ежедневного отчета"""

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

    weekly_log = models.ForeignKey(
        to=WeeklyLog,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Недельный отчет',
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Пользователь',
        related_name='daily_logs',
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

    date = models.DateField(
        default=timezone.now,
        verbose_name='Дата замера',
    )

    class Meta:
        verbose_name = 'Дневной замер состояния'
        verbose_name_plural = 'Дневные замеры состояния'
        ordering = ['-updated_at']

        unique_together = ('user', 'date')


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
        verbose_name = 'Замер уровня глюкозы'
        verbose_name_plural = 'Замеры уровня глюкозы'

    def __str__(self):
        return f'{self.user}:{self.updated_at}:{self.level}'


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

    class Meta:
        verbose_name = 'Замер давления'
        verbose_name_plural = 'Замеры давления'

    def __str__(self):
        return f'{self.user}:{self.updated_at}:{self.systolic}/{self.diastolic}'


class BodyTemperature(AutoDateMixin):
    """Модель для замера температуры тела"""

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
        related_name='body_temperatures',
    )

    temperature = models.FloatField(
        verbose_name='Температура тела',
        validators=[validate_positive_float],
    )

    class Meta:
        verbose_name = 'Температура тела'
        verbose_name_plural = 'Температуры тела'

    def __str__(self):
        return f'{self.user}:{self.updated_at}:{self.temperature}'
