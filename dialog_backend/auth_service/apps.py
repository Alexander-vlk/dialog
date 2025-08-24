from django.apps import AppConfig


class AuthServiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "auth_service"
    verbose_name = "Сервис авторизации"
