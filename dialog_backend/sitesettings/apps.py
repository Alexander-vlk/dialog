from django.apps import AppConfig


class SitesettingsConfig(AppConfig):
    """Конфигурация приложения"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "sitesettings"
    verbose_name = "Настройки сайта"
