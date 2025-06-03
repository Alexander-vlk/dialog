import pytest

from data_tracking.tests.factories import DailyLogFactory, MonthlyLogFactory, WeeklyLogFactory


@pytest.fixture
def monthly_log(user):
    """Фикстура еженедельного отчета"""
    return MonthlyLogFactory(user=user)


@pytest.fixture
def weekly_log(user, monthly_log):
    """Фикстура еженедельного отчета, привязанного к ежемесячному отчету"""
    return WeeklyLogFactory(user=user, monthly_log=monthly_log)


@pytest.fixture
def daily_log(user, weekly_log):
    """Фикстура ежедневного отчета, привязанного к недельному отчету"""
    return DailyLogFactory(user=user, weekly_log=weekly_log)


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


@pytest.fixture
def user_with_daily_log(user, daily_log):
    """Фикстура пользователя с актуальным ежедневным отчетом"""
    daily_log.user = user
    daily_log.save()
    return user
