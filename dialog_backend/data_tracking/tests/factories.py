from django.utils import timezone
from factory.fuzzy import FuzzyFloat
from factory.django import DjangoModelFactory

from data_tracking.models import MonthlyLog, WeeklyLog


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
