from django.contrib.auth.models import User
from django.utils import timezone

from data_tracking.models import MonthlyLog, WeeklyLog, DailyLog


def create_logs_for_new_user(user: User):
    """Создает отчеты для нового пользователя"""
    monthly_log = MonthlyLog.objects.create(
        user=user,
        month=timezone.now().month,
    )

    weekly_log = WeeklyLog.objects.create(
        user=user,
        monthly_log=monthly_log,
        weight=0,
        bmi=0,
        ketones=0,
        week_start=timezone.now(),
        week_end=timezone.now() + timezone.timedelta(days=7),
    )

    DailyLog.objects.create(
        user=user,
        weekly_log=weekly_log,
        calories_count=0,
        proteins_count=0,
        fats_count=0,
        carbs_count=0,
    )
