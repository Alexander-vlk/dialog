from django.urls import path

from sitesettings.views.public import CallToActionBlockView, FeatureAPIView


urlpatterns = [
    path('call-action-block/', CallToActionBlockView.as_view(), name='call_action_block'),
    path('features/', FeatureAPIView.as_view(), name='features'),
]
