from django.core.management import BaseCommand

from cabinet.services import execute_calculate_streak_for_users


class Command(BaseCommand):
    """Команда по подсчету и сохранению ударного режима в Redis"""

    def handle(self, *args, **options):
        """Выполнить команду"""
        execute_calculate_streak_for_users()
