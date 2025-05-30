import pytest

from data_tracking.tests.factories import MonthlyLogFactory


@pytest.fixture
def monthly_log(user):
    """Фикстура еженедельного отчета"""
    return MonthlyLogFactory(user=user)
