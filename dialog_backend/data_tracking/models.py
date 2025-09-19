from django.db import models
from django.utils import timezone

from auth_service.models import AppUser
from common_utils.mixins import AutoDateMixin
from common_utils.validators import validate_positive_float


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
        to=AppUser,
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
    year = models.PositiveSmallIntegerField(
        verbose_name='Год',
        default=timezone.now().year,
    )

    class Meta:
        verbose_name = 'Месячный замер состояния'
        verbose_name_plural = 'Месячные замеры состояния'
        unique_together = ('user', 'month', 'year')

    def __str__(self):
        return f'Отчет за {self.MONTH_CHOICES[self.month].lower()} {self.year}'


class WeeklyLog(AutoDateMixin):
    """Модель еженедельного отчета"""

    user = models.ForeignKey(
        to=AppUser,
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
    bmi = models.DecimalField(
        max_digits=5,
        decimal_places=1,
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
        unique_together = ('user', 'week_start', 'week_end')

    def __str__(self):
        return f'Отчет за неделю {self.week_start.strftime("%d.%m.%Y")} - {self.week_end.strftime("%d.%m.%Y")}'

    @property
    def is_filled(self):
        """Заполнен ли отчет"""
        return any(
            [
                self.weight,
                self.bmi,
                self.ketones,
            ]
        )


class Mood(AutoDateMixin):
    """Модель самочувствия"""

    name = models.CharField(
        max_length=50,
        verbose_name='Название настроения',
    )
    color = models.CharField(
        max_length=50,
        verbose_name='Цвет',
        help_text='Tailwind-класс',
        default='',
        blank=True,
    )
    bg_color = models.CharField(
        max_length=50,
        verbose_name='Цвет фона',
        help_text='Tailwind-класс',
        default='',
        blank=True,
    )

    class Meta:
        verbose_name = 'Настроение'
        verbose_name_plural = 'Настроения'

    def __str__(self):
        return self.name


class DailyLog(AutoDateMixin):
    """Модель ежедневного отчета"""

    TERRIBLE = 1
    BAD = 2
    NORMAL = 3
    GOOD = 4
    GREAT = 5
    GENERAL_HEALTH_CHOICES = {
        TERRIBLE: 'Ужасное',
        BAD: 'Плохое',
        NORMAL: 'Нормальное',
        GOOD: 'Хорошее',
        GREAT: 'Прекрасное',
    }

    user = models.ForeignKey(
        to=AppUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Пользователь',
        related_name='daily_logs',
    )
    weekly_log = models.ForeignKey(
        to=WeeklyLog,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Недельный отчет',
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
    mood = models.SmallIntegerField(
        verbose_name='Настроение',
        choices=GENERAL_HEALTH_CHOICES,
        default=NORMAL,
    )
    health = models.ManyToManyField(
        to=Mood,
        related_name='daily_logs',
        blank=True,
        verbose_name='Самочувствие',
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

    def __str__(self):
        return f'Отчет за {self.date}'

    @property
    def is_filled(self):
        return any(
            [
                self.calories_count,
                self.proteins_count,
                self.fats_count,
                self.carbs_count,
                self.physical_activity,
            ]
        )


class Glucose(AutoDateMixin):
    """Модель для уровня глюкозы"""

    user = models.ForeignKey(
        to=AppUser,
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
        to=AppUser,
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
        to=AppUser,
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
