from django.urls import path

from data_tracking.views.private import PressureAPIView


urlpatterns = [
    path('pressure/', PressureAPIView.as_view(), name='pressure'),
]
