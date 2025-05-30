import pytest

from data_tracking.tests.factories import MonthlyLogFactory, WeeklyLogFactory


@pytest.fixture
def monthly_log(user):
    """Фикстура еженедельного отчета"""
    return MonthlyLogFactory(user=user)


@pytest.fixture
def weekly_log(user, monthly_log):
    """Фикстура еженедельного отчета, привязанного к ежемесячному отчету"""
    return WeeklyLogFactory(user=user, monthly_log=monthly_log)


@pytest.fixture
def user_with_monthly_log(user, monthly_log):
    """Фикстура пользователя с актуальным ежемесячным отчетом"""
    monthly_log.user = user
    monthly_log.save()

    return user


@pytest.fixture
def user_with_weekly_log(user, weekly_log):
    """Фикстура пользователя с актуальным еженедельным отчетом"""
    weekly_log.user = user
    weekly_log.save()
    return user
