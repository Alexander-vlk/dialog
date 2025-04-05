from django.urls import path

from data_tracking.templateviews import glucose, pressure, temperature


urlpatterns = [
    path('glucose/new', glucose, name='new_glucose'),
    path('pressure/new', pressure, name='new_pressure'),
    path('temperature/new', temperature, name='new_temperature'),
]
