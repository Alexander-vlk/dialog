import logging

from django.core.management import BaseCommand
from django.db.models import Q
from django.utils import timezone

from auth_service.models import AppUser
from constants import BATCH_SIZE
from data_tracking.models import DailyLog, WeeklyLog

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Команда по созданию ежедневных отчетов для всех пользователей"""

    def handle(self, *args, **options):
        """Метод выполнения команды"""
        logger.info('Start command create_daily_log')

        users = AppUser.objects.filter(
            Q(is_staff=False) | Q(is_superuser=True),
            is_active=True,
        )

        weekly_logs = {
            weekly_log.user.id: weekly_log
            for weekly_log in WeeklyLog.objects.filter(
                week_start__lte=timezone.now(), week_end__gt=timezone.now()
            )
        }

        daily_logs = [
            DailyLog(
                user=user,
                weekly_log=weekly_logs.get(user.id),
                calories_count=0,
                proteins_count=0,
                fats_count=0,
                carbs_count=0,
            )
            for user in users
            if not DailyLog.objects.filter(user=user, date=timezone.now()).exists()
        ]

        for user in users:
            if user.id not in weekly_logs:
                logger.info("There's no weekly log for user with id %s", user.id)

        DailyLog.objects.bulk_create(daily_logs, batch_size=BATCH_SIZE)

        logger.info('Finish command create_daily_log')
