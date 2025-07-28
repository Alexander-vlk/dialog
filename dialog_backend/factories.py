import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """Фабрика пользователя"""

    class Meta:
        model = User
