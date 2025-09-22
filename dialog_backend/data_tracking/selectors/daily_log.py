from django.core.cache import cache

from auth_service.models import AppUser
from data_tracking.models import DailyLog
from data_tracking.types import DailyLogFillStatus


def get_daily_logs_fill_status(user: AppUser) -> list[DailyLogFillStatus]:
    """Получить статусы заполнения дневных отчетов по конкретному пользователю"""
    daily_log_status_cache_key = f'daily_logs:statuses:{user.id}'
    fill_statuses = cache.get(daily_log_status_cache_key) or []
    if not fill_statuses:
        for daily_log in DailyLog.objects.filter(user=user):
            fill_statuses.append({
                'date': daily_log.date,
                'is_filled': daily_log.is_filled,
            })

        cache.set(daily_log_status_cache_key, fill_statuses, 24*60*60*60)

    return fill_statuses
