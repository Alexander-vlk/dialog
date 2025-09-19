from data_tracking.models import DailyLog, Mood
from data_tracking.types import DailyLogData


def update_daily_log(daily_log: DailyLog, data: DailyLogData) -> None:
    """Обновить дневной отчет"""
    daily_log.calories_count = data['calories_count']
    daily_log.proteins_count = data['proteins_count']
    daily_log.fats_count = data['fats_count']
    daily_log.carbs_count = data['carbs_count']
    daily_log.mood = data['mood']
    daily_log.physical_activity = data['physical_activity']
    daily_log.additional_info = data['additional_info']
    daily_log.date = data['date']
    for health_instance in Mood.objects.filter(id__in=data['health_ids']):
        daily_log.health.add(health_instance)

    daily_log.save()
