from django.contrib import admin

from sitesettings.models.site_settings import MainPageSettings
from sitesettings.models.main_page import (
    CallToActionBlock,
    Feature,
    HeroActionBlock,
    MainPageFAQ,
    SliderImage,
)


@admin.register(MainPageSettings)
class MainPageSettingsAdmin(admin.ModelAdmin):
    """Админ для модели MainPageSettings"""

    list_display = (
        'id',
        'max_slider_images',
        'max_advantages_count',
        'max_functions_count',
        'max_reviews_count',
        'max_faqs_count',
    )


@admin.register(CallToActionBlock)
class CallToActionBlockAdmin(admin.ModelAdmin):
    """Админ для модели CallToActionBlock"""

    list_display = (
        'id',
        'action_text',
        'show_on_main_page',
    )
    list_filter = ('show_on_main_page',)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    """Админ для модели Feature"""

    list_display = (
        'name',
        'description',
    )


@admin.register(HeroActionBlock)
class HeroActionBlockAdmin(admin.ModelAdmin):
    """Админ для модели HeroActionBlock"""

    list_display = (
        'slogan',
        'short_description',
        'show_on_main_page',
    )
    list_filter = ('show_on_main_page',)


@admin.register(MainPageFAQ)
class MainPageFAQAdmin(admin.ModelAdmin):
    """Админ для модели MainPageFAQ"""

    list_display = (
        'id',
        'question',
        'answer',
    )

@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    """Админ для модели SliderImage"""

    list_display = (
        'id',
        'alt',
        'show_on_main_page',
    )
    list_filter = ('show_on_main_page',)
