from django.urls import path

from data_tracking.views.private import (
    AvgBJUApiView,
    AverageGlucoseDataAPIView,
    BodyTemperatureAPIView,
    CaloriesAPIView,
    GlucoseAPIView,
    HealthAPIView,
    PressureAPIView,
    WeeklyLogAPIView,
)

urlpatterns = [
    path('glucose/average/', AverageGlucoseDataAPIView.as_view(), name='average-glucose'),
    path('body-temperature/', BodyTemperatureAPIView.as_view(), name='body_temperature'),
    path('calories/', CaloriesAPIView.as_view(), name='calories'),
    path('glucose/', GlucoseAPIView.as_view(), name='glucose'),
    path('pressure/', PressureAPIView.as_view(), name='pressure'),
    path('bju/average/', AvgBJUApiView.as_view(), name='bju-average'),
    path('health/', HealthAPIView.as_view(), name='health'),

    path('weekly-log/', WeeklyLogAPIView.as_view(), name='weekly_log'),
]
