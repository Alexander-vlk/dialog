from django.utils import timezone
from factory.django import DjangoModelFactory

from data_tracking.models import MonthlyLog


class MonthlyLogFactory(DjangoModelFactory):
    """Фабрика модели MonthlyLog"""

    class Meta:
        model = MonthlyLog

    month = timezone.now().month
