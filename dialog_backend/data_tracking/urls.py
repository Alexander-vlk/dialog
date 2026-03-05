from django.urls import path, include
from rest_framework.routers import SimpleRouter

from data_tracking.views import MoodViewSet, TemperatureViewSet

data_tracking_router = SimpleRouter()
data_tracking_router.register('mood', MoodViewSet)
data_tracking_router.register('temperature', TemperatureViewSet, basename='temperature')

urlpatterns = [
    path('', include(data_tracking_router.urls)),
]
