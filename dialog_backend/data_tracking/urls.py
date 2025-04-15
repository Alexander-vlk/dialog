from django.urls import path

from data_tracking.views.private import BodyTemperatureAPIView, GlucoseAPIView, PressureAPIView

urlpatterns = [
    path('body-temperature/', BodyTemperatureAPIView.as_view(), name='body-temperature'),
    path('glucose/', GlucoseAPIView.as_view(), name='glucose'),
    path('pressure/', PressureAPIView.as_view(), name='pressure'),
]
