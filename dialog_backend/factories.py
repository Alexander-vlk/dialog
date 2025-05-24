import factory
from django.contrib.auth.models import User

from cabinet.models import UserProfile


class UserFactory(factory.django.DjangoModelFactory):
    """Фабрика пользователя"""

    class Meta:
        model = User


class UserProfileFactory(factory.django.DjangoModelFactory):
    """Фабрика профиля пользователя"""

    class Meta:
        model = UserProfile
