from django.urls import path

from cabinet.views import TreatmentTypeAPIView

urlpatterns = [
    path('treatment-types/', TreatmentTypeAPIView.as_view(), name='treatment_types'),
]
