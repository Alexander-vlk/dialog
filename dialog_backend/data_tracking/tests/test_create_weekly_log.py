import pytest
from django.core.management import call_command
from django.utils import timezone

from data_tracking.models import WeeklyLog, MonthlyLog

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def user_with_burning_weekly_log(user_with_weekly_log, weekly_log):
    """Фикстура еженедельного отчета, который на следующий день перестанет быть актуален"""
    weekly_log.week_end = timezone.now()
    weekly_log.save()
    return weekly_log


def test_weekly_log_creates(user_with_monthly_log):
    """
    Arrange: Пользователь без актуального еженедельного отчета
    Act: Запуск команды create_weekly_log
    Assert: Еженедельный отчет создался успешно
    """
    assert not WeeklyLog.objects.exists()
    call_command('create_weekly_log')
    assert WeeklyLog.objects.exists()


def test_weekly_log_creates_for_users_without_monthly_log(user):
    """
    Arrange: Пользователь без актуального еженедельного отчета и без ежемесячного отчета
    Act: Запуск команды create_weekly_log
    Assert: Еженедельный отчет создался успешно
    """
    assert not WeeklyLog.objects.exists()
    assert not MonthlyLog.objects.exists()
    call_command('create_weekly_log')
    assert WeeklyLog.objects.exists()


def test_weekly_log_doesnt_create_for_users_with_actual_weekly_log(user_with_weekly_log):
    """
    Arrange: Пользователь с актуальным еженедельным отчетом
    Act: Запуск команды create_weekly_log
    Assert: Еженедельный отчет не создан
    """
    call_command('create_weekly_log')
    assert WeeklyLog.objects.exists()


def test_weekly_log_doesnt_create_for_inactive_users(inactive_user):
    """
    Arrange: Неактивный пользователь
    Act: Запуск команды create_weekly_log
    Assert: Еженедельный отчет не создан
    """
    assert not WeeklyLog.objects.exists()
    call_command('create_weekly_log')
    assert not WeeklyLog.objects.exists()


def test_weekly_log_doesnt_create_when_no_users_in_db():
    """
    Arrange: Отсутствие пользователей в БД
    Act: Запуск команды create_weekly_log
    Assert: Еженедельный отчет не создан
    """
    call_command('create_weekly_log')
    assert not WeeklyLog.objects.exists()


def test_user_has_one_weekly_log_between_two_weeks(user_with_burning_weekly_log):
    """
    Arrange: Пользователь с уже созданным еженедельным отчетом, который на следующий день уже будет неактуален
    Act: Запуск команды create_weekly_log
    Assert: Еженедельный отчет не создан
    """
    assert WeeklyLog.objects.exists()
    call_command('create_weekly_log')
    assert WeeklyLog.objects.count() == 1


def test_idempotency_for_command(user_with_weekly_log):
    """
    Arrange: Пользователь с актуальным еженедельным отчетом
    Act: Запуск команды create_weekly_log несколько раз
    Assert: Количество отчетов не изменилось
    """
    call_command('create_weekly_log')
    call_command('create_weekly_log')
    call_command('create_weekly_log')
    call_command('create_weekly_log')
    assert WeeklyLog.objects.count() == 1
