from celery import shared_task
from django.core.management import call_command


@shared_task
def health_check():
    """Celery-task проверки работоспособности celery в проекте"""
    return "Celery is working successfully"


@shared_task
def task_create_monthly_log():
    """Celery-task по созданию ежемесячного отчета"""
    call_command("create_monthly_log")


@shared_task
def task_create_weekly_log():
    """Celery-task по созданию еженедельного отчета"""
    call_command("create_weekly_log")


@shared_task
def task_create_daily_log():
    """Celery-task по созданию ежедневного отчета"""
    call_command("create_daily_log")
