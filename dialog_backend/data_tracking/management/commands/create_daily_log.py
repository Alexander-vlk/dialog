import logging

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db.models import Q

from constants import BATCH_SIZE
from data_tracking.models import DailyLog


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Команда по созданию ежедневных отчетов для всех пользователей"""

    def handle(self, *args, **options):
        """Метод выполнения команды"""
        logger.info('Start command create_daily_log')

        users = User.objects.filter(
            Q(is_staff=False) | Q(is_superuser=True),
            is_active=True,
        )

        daily_logs = [
            DailyLog(
                user=user,
                calories_count=0,
                proteins_count=0,
                fats_count=0,
                carbs_count=0,
            )
            for user in users
        ]

        DailyLog.objects.bulk_create(daily_logs, batch_size=BATCH_SIZE)

        logger.info('Finish command create_daily_log')
