from celery import shared_task
from django.core.management import call_command


@shared_task
def task_calculate_streak_for_users():
    """Периодическая задача для запуска calculate_streak_for_users"""
    call_command('calculate_streak_for_users')
