from django.urls import path

from sitesettings.views.public import (
    CallToActionBlockView,
    FeatureAPIView,
    HeroActionBlockAPIView,
    MainPageFAQAPIView,
)


urlpatterns = [
    path('call-action-block/', CallToActionBlockView.as_view(), name='call_action_block'),
    path('features/', FeatureAPIView.as_view(), name='features'),
    path('hero-action-block/', HeroActionBlockAPIView.as_view(), name='hero_action_block'),
    path('main-page-faq/', MainPageFAQAPIView.as_view(), name='main_page_faq'),
]
