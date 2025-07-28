import pytest

from factories import UserFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def inactive_user():
    return UserFactory(is_active=False)
