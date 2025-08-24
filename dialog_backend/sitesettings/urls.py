from django.urls import path

from sitesettings.views.public import (
    AdvantageAPIView,
    CallToActionBlockView,
    FeatureAPIView,
    HeroActionBlockAPIView,
    MainPageFAQAPIView,
    RateAPIview,
    SliderImageAPIView,
)


urlpatterns = [
    path("advantages/", AdvantageAPIView.as_view(), name="advantages"),
    path(
        "call-action-block/", CallToActionBlockView.as_view(), name="call_action_block"
    ),
    path("features/", FeatureAPIView.as_view(), name="features"),
    path(
        "hero-action-block/", HeroActionBlockAPIView.as_view(), name="hero_action_block"
    ),
    path("main-page-faqs/", MainPageFAQAPIView.as_view(), name="main_page_faqs"),
    path("rates/", RateAPIview.as_view(), name="rates"),
    path("slider-images/", SliderImageAPIView.as_view(), name="slider_images"),
]
