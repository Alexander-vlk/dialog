from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cabinet.views import DiabetesTypeViewSet, TreatmentTypeViewSet, DiseaseViewSet

cabinet_router = SimpleRouter()
cabinet_router.register('diabetes_type', DiabetesTypeViewSet)
cabinet_router.register('treatment_type', TreatmentTypeViewSet)
cabinet_router.register('disease', DiseaseViewSet)

urlpatterns = [
    path('', include(cabinet_router.urls)),
]
