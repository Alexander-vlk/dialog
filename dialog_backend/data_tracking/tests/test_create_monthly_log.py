import pytest
from django.core.management import call_command

from data_tracking.models import MonthlyLog

pytestmark = [pytest.mark.django_db]


def test_monthly_logs_creates(user):
    """
    Arrange: Пользователь без актуального ежемесячного отчета
    Act: Запуск команды create_monthly_log
    Assert: Ежемесячный отчет для пользователя создан
    """
    assert not MonthlyLog.objects.exists()
    call_command("create_monthly_log")
    assert MonthlyLog.objects.exists()


def test_monthly_log_dont_create_for_inactive_users(inactive_user):
    """
    Arrange: Неактивный пользователь
    Act: Запуск команды create_monthly_log
    Assert: Еще один отчет для пользователя не создался
    """
    call_command("create_monthly_log")
    assert not MonthlyLog.objects.exists()


def test_monthly_log_dont_create_for_user_with_actual_log(user_with_monthly_log):
    """
    Arrange: Пользователь с актуальным ежемесячным отчетом
    Act: Запуск команды create_monthly_log
    Assert: Еще один отчет для пользователя не создался
    """
    call_command("create_monthly_log")
    assert MonthlyLog.objects.count() == 1


def test_monthly_log_dont_create_when_no_users_in_db():
    """
    Arrange: Отсутствие пользователей в БД
    Act: Запуск команды create_monthly_log
    Assert: Отчет не создался
    """
    call_command("create_monthly_log")
    assert not MonthlyLog.objects.exists()


def test_create_monthly_log_idempotency(user_with_monthly_log):
    """
    Arrange: Пользователь с актуальным ежемесячным отчетом
    Act: Запуск команды create_monthly_log 4 раза
    Assert: Количество отчетов в БД не изменилось
    """
    call_command("create_monthly_log")
    call_command("create_monthly_log")
    call_command("create_monthly_log")
    call_command("create_monthly_log")
    assert MonthlyLog.objects.count() == 1
