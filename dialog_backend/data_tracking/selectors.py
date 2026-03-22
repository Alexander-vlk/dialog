from typing import Callable

from django.db.models import Count, Avg, Min, Max

from auth_service.models import AppUser
from data_tracking.annotations import Median
from data_tracking.constants import AvailableIndicators
from data_tracking.dataclasses import AggregatedIndicatorData, DateBounds, DataForReport
from data_tracking.models import Temperature
from data_tracking.serializers import TemperatureSerializer


def _get_temperature_data(user: AppUser, date_bounds: DateBounds) -> AggregatedIndicatorData:
    """Получить собранные данные по температуре"""
    filtered_temperature_data = Temperature.objects.filter(
        user=user,
        measured_at__gte=date_bounds.date_start,
        measured_at__lte=date_bounds.date_end,
    )
    aggregated_values = (
        filtered_temperature_data
        .aggregate(
            total=Count('id', distinct=True),
            average=Avg('value'),
            median=Median('value'),
            min_value=Min('value'),
            max_value=Max('value'),
        )
    )
    min_temperature = TemperatureSerializer(
        filtered_temperature_data.filter(value=aggregated_values['min_value']).first()
    ).data
    max_temperature = TemperatureSerializer(
        filtered_temperature_data.filter(value=aggregated_values['max_value']).first()
    ).data
    return AggregatedIndicatorData(
        total=aggregated_values['total'],
        average_values={
            'value': aggregated_values['average'],
        },
        median_values={
            'value': aggregated_values['median'],
        },
        min_value=dict(min_temperature),
        max_value=dict(max_temperature),
    )


def _get_indicator_data(indicator: str, user: AppUser, date_bounds: DateBounds) -> AggregatedIndicatorData:
    """Получить собранные по показателю данные"""
    data_getter_by_indicator_name: dict[str, Callable] = {
        AvailableIndicators.TEMPERATURE: _get_temperature_data,
    }
    data_getter = data_getter_by_indicator_name[indicator]
    return data_getter(user, date_bounds)


def get_data_for_report(
    *,
    user: AppUser,
    indicators: list[str],
    date_bounds: DateBounds,
) -> DataForReport:
    """Получить данные для отчета"""
    aggregated_values = {
        indicator: _get_indicator_data(indicator, user, date_bounds)
        for indicator in indicators
    }
    return DataForReport(
        date_start=date_bounds.date_start,
        date_end=date_bounds.date_end,
        aggregated_values=aggregated_values,
    )
