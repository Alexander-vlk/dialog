from django.urls import path, include
from rest_framework.routers import SimpleRouter

from data_tracking.views import (
    MoodViewSet,
    TemperatureViewSet,
    GlucoseViewSet,
    HemoglobinViewSet,
    CholesterolViewSet,
    LipidProfileViewSet,
    MicroalbuminuriaViewSet,
    WeightViewSet,
    KetonesViewSet,
    MealViewSet,
    PhysicalActivityViewSet,
    NoteViewSet,
    MoodAppUserViewSet,
    HealthViewSet,
)
from data_tracking.views.indicators import HealthAppUserViewSet

data_tracking_router = SimpleRouter()
data_tracking_router.register('mood', MoodViewSet)
data_tracking_router.register('health', HealthViewSet)
data_tracking_router.register('temperature', TemperatureViewSet, basename='temperature')
data_tracking_router.register('glucose', GlucoseViewSet, basename='glucose')
data_tracking_router.register('hemoglobin', HemoglobinViewSet, basename='hemoglobin')
data_tracking_router.register('cholesterol', CholesterolViewSet, basename='cholesterol')
data_tracking_router.register('lipid_profile', LipidProfileViewSet, basename='lipid_profile')
data_tracking_router.register('microalbuminuria', MicroalbuminuriaViewSet, basename='microalbuminuria')
data_tracking_router.register('weight', WeightViewSet, basename='weight')
data_tracking_router.register('ketones', KetonesViewSet, basename='ketones')
data_tracking_router.register('meals', MealViewSet, basename='meals')
data_tracking_router.register('physical_activity', PhysicalActivityViewSet, basename='physical_activity')
data_tracking_router.register('note', NoteViewSet, basename='note')
data_tracking_router.register('mood_app_user', MoodAppUserViewSet, basename='mood_app_user')
data_tracking_router.register('health_app_user', HealthAppUserViewSet, basename='health_app_user')

urlpatterns = [
    path('', include(data_tracking_router.urls)),
]
