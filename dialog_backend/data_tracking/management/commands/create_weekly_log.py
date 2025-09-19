import logging

from django.core.management import BaseCommand
from django.db.models import Q
from django.utils import timezone

from auth_service.models import AppUser
from constants import BATCH_SIZE
from data_tracking.models import WeeklyLog, MonthlyLog

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Команда по созданию еженедельных отчетов"""

    def handle(self, *args, **options):
        """Метод выполнения команды"""
        logger.info('Start command create_weekly_log')

        users = AppUser.objects.filter(
            Q(is_staff=False) | Q(is_superuser=True),
            is_active=True,
        )

        monthly_logs = {
            monthly_log.user.id: monthly_log
            for monthly_log in MonthlyLog.objects.filter(
                month=timezone.now().month, year=timezone.now().year
            )
        }
        current_time = timezone.now()
        weekly_logs = [
            WeeklyLog(
                user=user,
                monthly_log=monthly_logs.get(user.id),
                weight=0,
                bmi=0,
                ketones=0,
                week_end=timezone.now() + timezone.timedelta(days=7),
            )
            for user in users
            if not WeeklyLog.objects.filter(
                user=user,
                week_start__lte=current_time,
                week_end__gte=current_time,
            ).exists()
        ]

        for user in users:
            if user.id not in monthly_logs:
                logger.info("There's no monthly log for user with id %s", user.id)

        WeeklyLog.objects.bulk_create(weekly_logs, batch_size=BATCH_SIZE)

        logger.info('Finish command create_weekly_log')
