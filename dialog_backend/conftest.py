import pytest

from django.contrib.auth.models import User

from factories import UserFactory, UserProfileFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def user_profile():
    return UserProfileFactory()
