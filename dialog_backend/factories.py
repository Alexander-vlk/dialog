import factory

from auth_service.models import AppUser


class AppUserFactory(factory.django.DjangoModelFactory):
    """Фабрика пользователя"""

    class Meta:
        model = AppUser
