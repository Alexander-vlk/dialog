from django.core.management.base import BaseCommand

from sitesettings.models import MainPageSettings


class Command(BaseCommand):
    """Команда создания базовых настроек главной страницы"""

    def handle(self, *args, **options):
        """Метод запуска команды"""
        MainPageSettings.objects.create(
            max_slider_images=4,
            max_advantages_count=4,
            max_functions_count=4,
            max_reviews_count=4,
            max_faqs_count=4,
        )
