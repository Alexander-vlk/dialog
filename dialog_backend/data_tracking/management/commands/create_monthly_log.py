import logging

from django.core.management import BaseCommand
from django.db.models import Q
from django.utils import timezone

from auth_service.models import AppUser
from constants import BATCH_SIZE
from data_tracking.models import MonthlyLog


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Команда по созданию ежемесячных отчетов"""

    def handle(self, *args, **options):
        """Метод выполнения команды"""
        logger.info("Start command create_monthly_log")

        users = AppUser.objects.filter(
            Q(is_staff=False) | Q(is_superuser=True),
            is_active=True,
        )

        monthly_logs = [
            MonthlyLog(
                user=user,
                month=timezone.now().month,
            )
            for user in users
            if not MonthlyLog.objects.filter(
                user=user, month=timezone.now().month
            ).exists()
        ]

        MonthlyLog.objects.bulk_create(monthly_logs, batch_size=BATCH_SIZE)

        logger.info("Finish command create_monthly_log")
