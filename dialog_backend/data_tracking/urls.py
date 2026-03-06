from django.urls import path, include
from rest_framework.routers import SimpleRouter

from data_tracking.views import MoodViewSet, TemperatureViewSet, GlucoseViewSet, HemoglobinViewSet, CholesterolViewSet, \
    LipidProfileViewSet, MicroalbuminuriaViewSet, WeightViewSet, KetonesViewSet, MealViewSet, PhysicalActivityViewSet, \
    NoteViewSet

data_tracking_router = SimpleRouter()
data_tracking_router.register('mood', MoodViewSet)
data_tracking_router.register('temperature', TemperatureViewSet, basename='temperature')
data_tracking_router.register('glucose', GlucoseViewSet, basename='glucose')
data_tracking_router.register('hemoglobin', HemoglobinViewSet, basename='hemoglobin')
data_tracking_router.register('cholesterol', CholesterolViewSet, basename='cholesterol')
data_tracking_router.register('lipid_profile', LipidProfileViewSet, basename='lipid_profile')
data_tracking_router.register('microalbuminuria', MicroalbuminuriaViewSet, basename='microalbuminuria')
data_tracking_router.register('weight', WeightViewSet, basename='weight')
data_tracking_router.register('ketones', KetonesViewSet, basename='ketones')
data_tracking_router.register('health', MealViewSet, basename='health')
data_tracking_router.register('physical_activity', PhysicalActivityViewSet, basename='physical_activity')
data_tracking_router.register('note', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(data_tracking_router.urls)),
]
