import pytest

from factories import UserFactory, UserProfileFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def user_profile():
    return UserProfileFactory()
