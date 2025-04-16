from django.urls import path

from data_tracking.views.private import (
    BodyTemperatureAPIView,
    GlucoseAPIView,
    PressureAPIView,
    WeeklyLogAPIView,
)

urlpatterns = [
    path('body-temperature/', BodyTemperatureAPIView.as_view(), name='body_temperature'),
    path('glucose/', GlucoseAPIView.as_view(), name='glucose'),
    path('pressure/', PressureAPIView.as_view(), name='pressure'),

    path('weekly-log/', WeeklyLogAPIView.as_view(), name='weekly_log'),
]
