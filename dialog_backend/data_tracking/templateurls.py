from django.urls import path

from data_tracking.templateviews import (
    glucose,
    pressure,
    temperature,
    daily_log,
    DailyLogListView,
)

urlpatterns = [
    path('glucose/new', glucose, name='new_glucose'),
    path('pressure/new', pressure, name='new_pressure'),
    path('temperature/new', temperature, name='new_temperature'),

    path('daily_log', daily_log, name='daily_log'),
    path('daily_log_list', DailyLogListView.as_view(), name='daily_log_list'),
]
