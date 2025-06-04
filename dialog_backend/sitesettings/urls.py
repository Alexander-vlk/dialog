from django.urls import path

from sitesettings.views.public import CallToActionBlockView


urlpatterns = [
    path('call-action-block/', CallToActionBlockView.as_view(), name='call_action_block'),
]
