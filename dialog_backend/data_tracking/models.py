from django.db import models
from django.utils import timezone

from auth_service.models import AppUser
from common_utils.mixins import AutoDateMixin
from common_utils.validators import validate_positive_float
from data_tracking.constants import CARBS_COUNT_BY_SINGLE_BREAD_UNIT


class Temperature(AutoDateMixin):
    """Температура"""

    value = models.FloatField(
        verbose_name='Значение (в Цельсия)', validators=[validate_positive_float]
    )
    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    measured_at = models.DateTimeField(
        verbose_name='Время замера', default=timezone.now
    )

    class Meta:
        verbose_name = 'Значение температуры'
        verbose_name_plural = 'Значения температуры'
        indexes = [
            models.Index(fields=['user', 'measured_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.measured_at}'


class Glucose(AutoDateMixin):
    """Глюкоза"""

    value = models.FloatField(
        verbose_name='Значение (ммоль/л)', validators=[validate_positive_float]
    )
    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    measured_at = models.DateTimeField(
        verbose_name='Время замера', default=timezone.now
    )

    class Meta:
        verbose_name = 'Значение уровня сахара в крови'
        verbose_name_plural = 'Значения уровня сахара в крови'
        indexes = [
            models.Index(fields=['user', 'measured_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.measured_at}'


class Hemoglobin(AutoDateMixin):
    """Гемоглобин"""

    value = models.PositiveSmallIntegerField(verbose_name='Значение (г/л)')
    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    measured_at = models.DateTimeField(
        verbose_name='Время замера', default=timezone.now
    )

    class Meta:
        verbose_name = 'Значение гемоглобина'
        verbose_name_plural = 'Значения гемоглобина'
        indexes = [
            models.Index(fields=['user', 'measured_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.measured_at}'


class Cholesterol(AutoDateMixin):
    """Холестерин"""

    value = models.FloatField(
        verbose_name='Значение (моль/л)', validators=[validate_positive_float]
    )
    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    measured_at = models.DateTimeField(
        verbose_name='Время замера', default=timezone.now
    )

    class Meta:
        verbose_name = 'Значение холестерина'
        verbose_name_plural = 'Значения холестерина'
        indexes = [
            models.Index(fields=['user', 'measured_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.measured_at}'


class LipidProfile(AutoDateMixin):
    """Липидный профиль"""

    value = models.FloatField(
        verbose_name='Значение (ммоль/л)', validators=[validate_positive_float]
    )
    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    measured_at = models.DateTimeField(
        verbose_name='Время замера', default=timezone.now
    )

    class Meta:
        verbose_name = 'Значение липидного профиля'
        verbose_name_plural = 'Значения липидного профиля'
        indexes = [
            models.Index(fields=['user', 'measured_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.measured_at}'


class Microalbuminuria(AutoDateMixin):
    """Микроальбуминурия"""

    value = models.FloatField(
        verbose_name='Значение (мг/сут)', validators=[validate_positive_float]
    )
    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    measured_at = models.DateTimeField(
        verbose_name='Время замера', default=timezone.now
    )

    class Meta:
        verbose_name = 'Значение микроальбуминурии'
        verbose_name_plural = 'Значения микроальбуминурии'
        indexes = [
            models.Index(fields=['user', 'measured_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.measured_at}'


class Weight(AutoDateMixin):
    """Вес"""

    value = models.PositiveSmallIntegerField(verbose_name='Значение (кг)')
    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    measured_at = models.DateTimeField(
        verbose_name='Время замера', default=timezone.now
    )

    class Meta:
        verbose_name = 'Значение веса'
        verbose_name_plural = 'Значения веса'
        indexes = [
            models.Index(fields=['user', 'measured_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.measured_at}'


class Ketones(AutoDateMixin):
    """Кетоны"""

    value = models.FloatField(
        verbose_name='Значение (ммоль/л)', validators=[validate_positive_float]
    )
    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    measured_at = models.DateTimeField(
        verbose_name='Время замера', default=timezone.now
    )

    class Meta:
        verbose_name = 'Значение кетонов'
        verbose_name_plural = 'Значения кетонов'
        indexes = [
            models.Index(fields=['user', 'measured_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.measured_at}'


class Meal(AutoDateMixin):
    """КБЖУ за прием пищи"""

    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    calories = models.PositiveSmallIntegerField(verbose_name='Калории')
    proteins = models.PositiveSmallIntegerField(verbose_name='Белки')
    carbs = models.PositiveSmallIntegerField(verbose_name='Жиры')
    fats = models.PositiveSmallIntegerField(verbose_name='Углеводы')
    eaten_at = models.DateTimeField(
        verbose_name='Время приема пищи', default=timezone.now
    )

    class Meta:
        verbose_name = 'Значение КБЖУ за прием пищи'
        verbose_name_plural = 'Значения КБЖУ за прием пищи'
        indexes = [
            models.Index(fields=['user', 'eaten_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.eaten_at}'

    @property
    def bread_units(self) -> float:
        """Хлебные единицы"""
        return self.carbs / CARBS_COUNT_BY_SINGLE_BREAD_UNIT


class PhysicalActivity(AutoDateMixin):
    """Физическая активность"""

    description = models.CharField(verbose_name='Описание', max_length=1000)
    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    measured_at = models.DateTimeField(
        verbose_name='Время замера', default=timezone.now
    )

    class Meta:
        verbose_name = 'Запись о физической активности'
        verbose_name_plural = 'Записи о физической активности'
        indexes = [
            models.Index(fields=['user', 'measured_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.measured_at}'


class Note(AutoDateMixin):
    """Физическая активность"""

    description = models.CharField(verbose_name='Описание', max_length=1000)
    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    measured_at = models.DateTimeField(
        verbose_name='Время замера',
        default=timezone.now,
    )

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        indexes = [
            models.Index(fields=['user', 'measured_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.measured_at}'


class Mood(AutoDateMixin):
    """Настроение"""

    name = models.CharField(verbose_name='Название', max_length=1000)
    text_color = models.CharField(
        verbose_name='Цвет', max_length=20, help_text='TailwindCSS-стиль'
    )
    background_color = models.CharField(
        verbose_name='Цвет', max_length=20, help_text='TailwindCSS-стиль'
    )

    class Meta:
        verbose_name = 'Настроение'
        verbose_name_plural = 'Справочник настроений'
        ordering = ['name']

    def __str__(self):
        return self.name


class MoodAppUser(AutoDateMixin):
    """Прокси-модель связки настроения и пользователя"""

    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    mood = models.ForeignKey(Mood, verbose_name='Настроение', on_delete=models.PROTECT)
    measured_at = models.DateTimeField(
        verbose_name='Время замера', default=timezone.now
    )

    class Meta:
        verbose_name = 'Связка пользователя и настроения'
        verbose_name_plural = 'Связки пользователя и настроения'
        indexes = [
            models.Index(fields=['user', 'mood', 'measured_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.mood.name} - {self.measured_at}'


class Health(AutoDateMixin):
    """Самочувствие"""

    name = models.CharField(verbose_name='Название', max_length=1000)
    text_color = models.CharField(
        verbose_name='Цвет',
        max_length=20,
        help_text='TailwindCSS-стиль',
    )
    background_color = models.CharField(
        verbose_name='Цвет',
        max_length=20,
        help_text='TailwindCSS-стиль',
    )

    class Meta:
        verbose_name = 'Самочувствие'
        verbose_name_plural = 'Справочник типов самочувствия'
        ordering = ['name']

    def __str__(self):
        return self.name


class HealthAppUser(AutoDateMixin):
    """Прокси-модель связки самочувствия и пользователя"""

    user = models.ForeignKey(
        AppUser, verbose_name='Пользователь', on_delete=models.PROTECT
    )
    health = models.ForeignKey(Health, verbose_name='Самочувствие', on_delete=models.PROTECT)
    measured_at = models.DateTimeField(
        verbose_name='Время замера',
        default=timezone.now,
    )

    class Meta:
        verbose_name = 'Связка пользователя и самочувствия'
        verbose_name_plural = 'Связки пользователя и самочувствия'
        indexes = [
            models.Index(fields=['user', 'health', 'measured_at']),
        ]

    def __str__(self):
        return f'{self.user.username} {self.health.name} - {self.measured_at}'
