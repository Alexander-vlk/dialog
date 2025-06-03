from django.utils import timezone
from factory.fuzzy import FuzzyFloat, FuzzyInteger
from factory.django import DjangoModelFactory

from data_tracking.models import DailyLog, MonthlyLog, WeeklyLog


class MonthlyLogFactory(DjangoModelFactory):
    """Фабрика модели MonthlyLog"""

    class Meta:
        model = MonthlyLog

    month = timezone.now().month


class WeeklyLogFactory(DjangoModelFactory):
    """Фабрика модели WeeklyLog"""

    class Meta:
        model = WeeklyLog

    weight = FuzzyFloat(0)
    bmi = FuzzyFloat(0)
    ketones = FuzzyFloat(0)


class DailyLogFactory(DjangoModelFactory):
    """Фабрика модели DailyLog"""

    class Meta:
        model = DailyLog

    calories_count = FuzzyInteger(500, 4500)

    proteins_count = FuzzyInteger(20, 200)
    fats_count = FuzzyInteger(20, 200)
    carbs_count = FuzzyInteger(20, 200)

    date = timezone.now().date
