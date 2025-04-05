from django.urls import path

from data_tracking.templateviews import glucose, pressure, temperature, daily_log, get_glucose_for_plot


urlpatterns = [
    path('glucose/new', glucose, name='new_glucose'),
    path('pressure/new', pressure, name='new_pressure'),
    path('temperature/new', temperature, name='new_temperature'),

    path('daily_log', daily_log, name='daily_log'),

    path('glucose_data/', get_glucose_for_plot, name='get_glucose_for_plot'),
]
