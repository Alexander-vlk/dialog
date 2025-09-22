from django.urls import path

from data_tracking.views import MoodAPIView
from data_tracking.views.private import (
    AvgBJUApiView,
    AverageGlucoseDataAPIView,
    BodyTemperatureAPIView,
    CaloriesAPIView,
    DailyLogAPIView,
    GlucoseAPIView,
    HealthAPIView,
    PressureAPIView,
    WeeklyLogAPIView,
    ListDailyLogAPIView,
)

urlpatterns = [
    path('glucose/average/', AverageGlucoseDataAPIView.as_view(), name='average-glucose'),
    path('body-temperature/', BodyTemperatureAPIView.as_view(), name='body_temperature'),
    path('calories/', CaloriesAPIView.as_view(), name='calories'),
    path('glucose/', GlucoseAPIView.as_view(), name='glucose'),
    path('pressure/', PressureAPIView.as_view(), name='pressure'),
    path('bju/average/', AvgBJUApiView.as_view(), name='bju-average'),
    path('health/', HealthAPIView.as_view(), name='health'),
    path('mood/', MoodAPIView.as_view(), name='mood'),
    path('daily-logs/current/', DailyLogAPIView.as_view(), name='current_daily_log'),
    path('daily-logs/', ListDailyLogAPIView.as_view(), name='daily_log'),
    path('weekly-logs/', WeeklyLogAPIView.as_view(), name='weekly_log'),
]
