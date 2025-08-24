from django.contrib import admin
from django.db import models
from django import forms

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
        "id",
        "max_slider_images",
        "max_advantages_count",
        "max_functions_count",
        "max_reviews_count",
        "max_faqs_count",
    )


@admin.register(CallToActionBlock)
class CallToActionBlockAdmin(admin.ModelAdmin):
    """Админ для модели CallToActionBlock"""

    list_display = (
        "id",
        "action_text",
        "show_on_main_page",
    )
    list_display_links = ["action_text"]
    list_filter = ("show_on_main_page",)
    formfield_overrides = {
        models.CharField: {
            "widget": forms.Textarea(),
        },
    }


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    """Админ для модели Feature"""

    list_display = (
        "name",
        "description",
    )
    formfield_overrides = {
        models.CharField: {
            "widget": forms.Textarea(),
        },
    }


@admin.register(HeroActionBlock)
class HeroActionBlockAdmin(admin.ModelAdmin):
    """Админ для модели HeroActionBlock"""

    list_display = (
        "slogan",
        "short_description",
        "show_on_main_page",
    )
    list_filter = ("show_on_main_page",)
    formfield_overrides = {
        models.CharField: {
            "widget": forms.Textarea(),
        },
    }


@admin.register(MainPageFAQ)
class MainPageFAQAdmin(admin.ModelAdmin):
    """Админ для модели MainPageFAQ"""

    list_display = (
        "id",
        "question",
        "answer",
    )
    list_display_links = ["question"]
    formfield_overrides = {
        models.CharField: {
            "widget": forms.Textarea(),
        },
    }


@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    """Админ для модели SliderImage"""

    list_display = (
        "id",
        "alt",
        "show_on_main_page",
    )
    list_display_links = ["alt"]
    list_filter = ("show_on_main_page",)
    formfield_overrides = {
        models.CharField: {
            "widget": forms.Textarea(),
        },
    }
