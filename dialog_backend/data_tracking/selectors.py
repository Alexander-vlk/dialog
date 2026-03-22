from statistics import median
from typing import Callable

from django.db.models import Count, Avg, Min, Max, Q

from auth_service.models import AppUser
from data_tracking.annotations import Median
from data_tracking.constants import AvailableIndicators
from data_tracking.dataclasses import AggregatedIndicatorData, DateBounds, DataForReport
from data_tracking.models import Temperature, Pressure, Glucose, Hemoglobin, Cholesterol, LipidProfile, \
    Microalbuminuria, Weight, Ketones, Meal
from data_tracking.serializers import TemperatureSerializer, PressureSerializer


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
    min_temperature_db_instance = filtered_temperature_data.filter(value=aggregated_values['min_value']).first()
    max_temperature_db_instance = filtered_temperature_data.filter(value=aggregated_values['max_value']).first()
    min_temperature = (
        dict(TemperatureSerializer(min_temperature_db_instance).data) if min_temperature_db_instance else None
    )
    max_temperature = (
        dict(TemperatureSerializer(max_temperature_db_instance).data) if max_temperature_db_instance else None
    )
    return AggregatedIndicatorData(
        total=aggregated_values['total'],
        average_values={
            'value': aggregated_values['average'],
        },
        median_values={
            'value': aggregated_values['median'],
        },
        min_value=min_temperature,
        max_value=max_temperature,
    )


def _get_pressure_data(user: AppUser, date_bounds: DateBounds) -> AggregatedIndicatorData:
    """Получить собранные данные по давлению"""
    filtered_pressure_data = Pressure.objects.filter(
        user=user,
        measured_at__gte=date_bounds.date_start,
        measured_at__lte=date_bounds.date_end,
    )
    aggregated_values = (
        filtered_pressure_data
        .aggregate(
            total=Count('id', distinct=True),
            average_systolic=Avg('systolic'),
            median_systolic=Median('systolic'),
            average_diastolic=Median('diastolic'),
            median_diastolic=Median('diastolic'),
            min_systolic=Min('systolic'),
            max_systolic=Max('systolic'),
            min_diastolic=Min('diastolic'),
            max_diastolic=Max('diastolic'),
        )
    )
    min_pressure_db_instance = filtered_pressure_data.filter(
        Q(systolic=aggregated_values['min_systolic']) | Q(diastolic=aggregated_values['min_diastolic']),
    ).first()
    max_pressure_db_instance = filtered_pressure_data.filter(
        Q(systolic=aggregated_values['max_systolic']) | Q(diastolic=aggregated_values['max_diastolic']),
    ).first()
    min_pressure = dict(PressureSerializer(min_pressure_db_instance).data) if min_pressure_db_instance else None
    max_pressure = dict(PressureSerializer(max_pressure_db_instance).data) if max_pressure_db_instance else None
    return AggregatedIndicatorData(
        total=aggregated_values['total'],
        average_values={
            'systolic': aggregated_values['average_systolic'],
            'diastolic': aggregated_values['average_diastolic'],
        },
        median_values={
            'systolic': aggregated_values['median_systolic'],
            'diastolic': aggregated_values['median_diastolic'],
        },
        min_value=min_pressure,
        max_value=max_pressure,
    )


def _get_glucose_data(user: AppUser, date_bounds: DateBounds) -> AggregatedIndicatorData:
    """Получить собранные данные по уровню сахара в крови"""
    filtered_glucose_data = Glucose.objects.filter(
        user=user,
        measured_at__gte=date_bounds.date_start,
        measured_at__lte=date_bounds.date_end,
    )
    aggregated_values = (
        filtered_glucose_data
        .aggregate(
            total=Count('id', distinct=True),
            average=Avg('value'),
            median=Median('value'),
            min_value=Min('value'),
            max_value=Max('value'),
        )
    )
    min_glucose_db_instance = filtered_glucose_data.filter(value=aggregated_values['min_value']).first()
    max_glucose_db_instance = filtered_glucose_data.filter(value=aggregated_values['max_value']).first()
    min_glucose = dict(TemperatureSerializer(min_glucose_db_instance).data) if min_glucose_db_instance else None
    max_glucose = dict(TemperatureSerializer(max_glucose_db_instance).data) if max_glucose_db_instance else None
    return AggregatedIndicatorData(
        total=aggregated_values['total'],
        average_values={
            'value': aggregated_values['average'],
        },
        median_values={
            'value': aggregated_values['median'],
        },
        min_value=min_glucose,
        max_value=max_glucose,
    )


def _get_hemoglobin_data(user: AppUser, date_bounds: DateBounds) -> AggregatedIndicatorData:
    """Получить собранные данные по гемоглобину"""
    filtered_hemoglobin_data = Hemoglobin.objects.filter(
        user=user,
        measured_at__gte=date_bounds.date_start,
        measured_at__lte=date_bounds.date_end,
    )
    aggregated_values = (
        filtered_hemoglobin_data
        .aggregate(
            total=Count('id', distinct=True),
            average=Avg('value'),
            median=Median('value'),
            min_value=Min('value'),
            max_value=Max('value'),
        )
    )
    min_hemoglobin_db_instance = filtered_hemoglobin_data.filter(value=aggregated_values['min_value']).first()
    max_hemoglobin_db_instance = filtered_hemoglobin_data.filter(value=aggregated_values['max_value']).first()
    min_hemoglobin = (
        dict(TemperatureSerializer(min_hemoglobin_db_instance).data) if min_hemoglobin_db_instance else None
    )
    max_hemoglobin = (
        dict(TemperatureSerializer(max_hemoglobin_db_instance).data) if max_hemoglobin_db_instance else None
    )
    return AggregatedIndicatorData(
        total=aggregated_values['total'],
        average_values={
            'value': aggregated_values['average'],
        },
        median_values={
            'value': aggregated_values['median'],
        },
        min_value=min_hemoglobin,
        max_value=max_hemoglobin,
    )


def _get_cholesterol_data(user: AppUser, date_bounds: DateBounds) -> AggregatedIndicatorData:
    """Получить собранные данные по уровню холестерина"""
    filtered_cholesterol_data = Cholesterol.objects.filter(
        user=user,
        measured_at__gte=date_bounds.date_start,
        measured_at__lte=date_bounds.date_end,
    )
    aggregated_values = (
        filtered_cholesterol_data
        .aggregate(
            total=Count('id', distinct=True),
            average=Avg('value'),
            median=Median('value'),
            min_value=Min('value'),
            max_value=Max('value'),
        )
    )
    min_cholesterol_db_instance = filtered_cholesterol_data.filter(value=aggregated_values['min_value']).first()
    max_cholesterol_db_instance = filtered_cholesterol_data.filter(value=aggregated_values['max_value']).first()
    min_cholesterol = (
        dict(TemperatureSerializer(min_cholesterol_db_instance).data) if min_cholesterol_db_instance else None
    )
    max_cholesterol = (
        dict(TemperatureSerializer(max_cholesterol_db_instance).data) if max_cholesterol_db_instance else None
    )
    return AggregatedIndicatorData(
        total=aggregated_values['total'],
        average_values={
            'value': aggregated_values['average'],
        },
        median_values={
            'value': aggregated_values['median'],
        },
        min_value=min_cholesterol,
        max_value=max_cholesterol,
    )


def _get_lipid_profile_data(user: AppUser, date_bounds: DateBounds) -> AggregatedIndicatorData:
    """Получить собранные данные по липидному профилю"""
    filtered_lipid_profile_data = LipidProfile.objects.filter(
        user=user,
        measured_at__gte=date_bounds.date_start,
        measured_at__lte=date_bounds.date_end,
    )
    aggregated_values = (
        filtered_lipid_profile_data
        .aggregate(
            total=Count('id', distinct=True),
            average=Avg('value'),
            median=Median('value'),
            min_value=Min('value'),
            max_value=Max('value'),
        )
    )
    min_lipid_profile_db_instance = filtered_lipid_profile_data.filter(value=aggregated_values['min_value']).first()
    max_lipid_profile_db_instance = filtered_lipid_profile_data.filter(value=aggregated_values['max_value']).first()
    min_lipid_profile = (
        dict(TemperatureSerializer(min_lipid_profile_db_instance).data) if min_lipid_profile_db_instance else None
    )
    max_lipid_profile = (
        dict(TemperatureSerializer(max_lipid_profile_db_instance).data) if max_lipid_profile_db_instance else None
    )
    return AggregatedIndicatorData(
        total=aggregated_values['total'],
        average_values={
            'value': aggregated_values['average'],
        },
        median_values={
            'value': aggregated_values['median'],
        },
        min_value=min_lipid_profile,
        max_value=max_lipid_profile,
    )


def _get_microalbuminuria_data(user: AppUser, date_bounds: DateBounds) -> AggregatedIndicatorData:
    """Получить собранные данные по микроальбуминурии"""
    filtered_microalbuminuria_data = Microalbuminuria.objects.filter(
        user=user,
        measured_at__gte=date_bounds.date_start,
        measured_at__lte=date_bounds.date_end,
    )
    aggregated_values = (
        filtered_microalbuminuria_data
        .aggregate(
            total=Count('id', distinct=True),
            average=Avg('value'),
            median=Median('value'),
            min_value=Min('value'),
            max_value=Max('value'),
        )
    )
    min_microalbuminuria_db_instance = filtered_microalbuminuria_data.filter(value=aggregated_values['min_value']).first()
    max_microalbuminuria_db_instance = filtered_microalbuminuria_data.filter(value=aggregated_values['max_value']).first()
    min_microalbuminuria = (
        dict(TemperatureSerializer(min_microalbuminuria_db_instance).data) if min_microalbuminuria_db_instance else None
    )
    max_microalbuminuria = (
        dict(TemperatureSerializer(max_microalbuminuria_db_instance).data) if max_microalbuminuria_db_instance else None
    )
    return AggregatedIndicatorData(
        total=aggregated_values['total'],
        average_values={
            'value': aggregated_values['average'],
        },
        median_values={
            'value': aggregated_values['median'],
        },
        min_value=min_microalbuminuria,
        max_value=max_microalbuminuria,
    )


def _get_weight_data(user: AppUser, date_bounds: DateBounds) -> AggregatedIndicatorData:
    """Получить собранные данные по весу"""
    filtered_weight_data = Weight.objects.filter(
        user=user,
        measured_at__gte=date_bounds.date_start,
        measured_at__lte=date_bounds.date_end,
    )
    aggregated_values = (
        filtered_weight_data
        .aggregate(
            total=Count('id', distinct=True),
            average=Avg('value'),
            median=Median('value'),
            min_value=Min('value'),
            max_value=Max('value'),
        )
    )
    min_weight_db_instance = filtered_weight_data.filter(value=aggregated_values['min_value']).first()
    max_weight_db_instance = filtered_weight_data.filter(value=aggregated_values['max_value']).first()
    min_weight = dict(TemperatureSerializer(min_weight_db_instance).data) if min_weight_db_instance else None
    max_weight = dict(TemperatureSerializer(max_weight_db_instance).data) if max_weight_db_instance else None
    return AggregatedIndicatorData(
        total=aggregated_values['total'],
        average_values={
            'value': aggregated_values['average'],
        },
        median_values={
            'value': aggregated_values['median'],
        },
        min_value=min_weight,
        max_value=max_weight,
    )


def _get_ketones_data(user: AppUser, date_bounds: DateBounds) -> AggregatedIndicatorData:
    """Получить собранные данные по уровню кетоновых тел"""
    filtered_ketones_data = Ketones.objects.filter(
        user=user,
        measured_at__gte=date_bounds.date_start,
        measured_at__lte=date_bounds.date_end,
    )
    aggregated_values = (
        filtered_ketones_data
        .aggregate(
            total=Count('id', distinct=True),
            average=Avg('value'),
            median=Median('value'),
            min_value=Min('value'),
            max_value=Max('value'),
        )
    )
    min_ketones_db_instance = filtered_ketones_data.filter(value=aggregated_values['min_value']).first()
    max_ketones_db_instance = filtered_ketones_data.filter(value=aggregated_values['max_value']).first()
    min_ketones = dict(TemperatureSerializer(min_ketones_db_instance).data) if min_ketones_db_instance else None
    max_ketones = dict(TemperatureSerializer(max_ketones_db_instance).data) if max_ketones_db_instance else None
    return AggregatedIndicatorData(
        total=aggregated_values['total'],
        average_values={
            'value': aggregated_values['average'],
        },
        median_values={
            'value': aggregated_values['median'],
        },
        min_value=min_ketones,
        max_value=max_ketones,
    )

def _get_meal_data(user: AppUser, date_bounds: DateBounds) -> AggregatedIndicatorData:
    """Получить собранные данные по приемам пищи"""
    # todo: переделать на получение отдельных приемов пищи с минимальным/максимальным значением отдельного параметра
    filtered_meal_data = Meal.objects.filter(
        user=user,
        measured_at__gte=date_bounds.date_start,
        measured_at__lte=date_bounds.date_end,
    )
    aggregated_values = filtered_meal_data.aggregate(
        total=Count('id', distinct=True),
        average_calories=Avg('calories'),
        median_calories=Median('calories'),
        average_proteins=Avg('proteins'),
        median_proteins=Median('proteins'),
        average_carbs=Avg('carbs'),
        median_carbs=Median('carbs'),
        average_fats=Avg('fats'),
        median_fats=Median('fats'),
    )
    return AggregatedIndicatorData(
        total=aggregated_values['total'],
        average_values={
            'value': aggregated_values['average'],
        },
        median_values={
            'value': aggregated_values['median'],
        },
        min_value=None,
        max_value=None,
    )


def _get_indicator_data(indicator: str, user: AppUser, date_bounds: DateBounds) -> AggregatedIndicatorData:
    """Получить собранные по показателю данные"""
    data_getter_by_indicator_name: dict[str, Callable] = {
        AvailableIndicators.TEMPERATURE: _get_temperature_data,
        AvailableIndicators.PRESSURE: _get_pressure_data,
        AvailableIndicators.GLUCOSE: _get_glucose_data,
        AvailableIndicators.HEMOGLOBIN: _get_hemoglobin_data,
        AvailableIndicators.CHOLESTEROL: _get_cholesterol_data,
        AvailableIndicators.LIPID_PROFILE: _get_lipid_profile_data,
        AvailableIndicators.MICROALBUMINURIA: _get_microalbuminuria_data,
        AvailableIndicators.WEIGHT: _get_weight_data,
        AvailableIndicators.KETONES: _get_ketones_data,
        AvailableIndicators.MEAL: _get_meal_data,
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
