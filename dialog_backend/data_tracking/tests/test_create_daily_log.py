import pytest
from django.core.management import call_command

from data_tracking.models import DailyLog

pytestmark = [pytest.mark.django_db]


def test_daily_log_creates(user):
    """
    Arrange: Пользователь без ежедневного отчета
    Act: Выполнение команды create_daily_log
    Assert: Ежедневный отчет создан
    """
    assert not DailyLog.objects.exists()
    call_command('create_daily_log')
    assert DailyLog.objects.exists()


def test_daily_log_dont_create_for_inactive_users(inactive_user):
    """
    Arrange: Неактивный пользователь
    Act: Запуск команды create_daily_log
    Assert: Отчет для пользователя не создался
    """
    call_command('create_daily_log')
    assert not DailyLog.objects.exists()


def test_daily_log_dont_create_for_user_with_actual_log(user_with_daily_log):
    """
    Arrange: Пользователь с актуальным ежедневным отчетом
    Act: Запуск команды create_daily_log
    Assert: Еще один отчет для пользователя не создался
    """
    call_command('create_daily_log')
    assert DailyLog.objects.count() == 1


def test_daily_log_dont_create_when_no_users_in_db():
    """
    Arrange: Отсутствие пользователей в БД
    Act: Запуск команды create_monthly_log
    Assert: Отчет не создался
    """
    call_command('create_daily_log')
    assert not DailyLog.objects.exists()


def test_create_monthly_log_idempotency(user_with_daily_log):
    """
    Arrange: Пользователь с актуальным ежедневным отчетом
    Act: Запуск команды create_monthly_log 4 раза
    Assert: Количество отчетов в БД не изменилось
    """
    call_command('create_daily_log')
    call_command('create_daily_log')
    call_command('create_daily_log')
    call_command('create_daily_log')
    assert DailyLog.objects.count() == 1
