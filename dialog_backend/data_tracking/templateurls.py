from django.urls import path

from data_tracking.templateviews import (
    glucose,
    pressure,
    temperature,
    daily_log,
    get_glucose_for_plot,
    get_pressure_for_plot,
    get_temperature_for_plot,
    DailyLogListView,
)

urlpatterns = [
    path('glucose/new', glucose, name='new_glucose'),
    path('pressure/new', pressure, name='new_pressure'),
    path('temperature/new', temperature, name='new_temperature'),

    path('daily_log', daily_log, name='daily_log'),
    path('daily_log_list', DailyLogListView.as_view(), name='daily_log_list'),

    path('glucose_data/', get_glucose_for_plot, name='get_glucose_for_plot'),
    path('pressure_data/', get_pressure_for_plot, name='get_pressure_for_plot'),
    path('temperature_data/', get_temperature_for_plot, name='get_temperature_for_plot'),
]
