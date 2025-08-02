import pytest

from factories import AppUserFactory


@pytest.fixture
def user():
    return AppUserFactory()


@pytest.fixture
def inactive_user():
    return AppUserFactory(is_active=False)
