from django.urls import path

from cabinet.views import DiabetesTypeAPIView, TreatmentTypeAPIView


urlpatterns = [
    path('treatment-types/', TreatmentTypeAPIView.as_view(), name='treatment_types'),
    path('diabetes-types/', DiabetesTypeAPIView.as_view(), name='diabetes_types'),
]
