from django.urls import path, include
from rest_framework.routers import SimpleRouter

from data_tracking.views import MoodViewSet

data_tracking_router = SimpleRouter()
data_tracking_router.register('mood', MoodViewSet)

urlpatterns = [
    path('', include(data_tracking_router.urls)),
]
