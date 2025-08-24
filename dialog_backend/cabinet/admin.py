from django import forms
from django.contrib import admin
from django.db import models

from cabinet.models import Advantage, Allergy, Disease, Rate, TreatmentType


@admin.register(TreatmentType)
class TreatmentTypeAdmin(admin.ModelAdmin):
    """Админ для модели TreatmentType"""

    list_display = ['name', 'slug']
    formfield_overrides = {
        models.CharField: {
            "widget": forms.Textarea(),
        },
        models.SlugField: {
            'widget': forms.Textarea(),
        },
    }



@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    """Админ для модели Advantage"""

    list_display = ["order_num", "title", "description"]
    list_display_links = ["title"]
    formfield_overrides = {
        models.CharField: {
            "widget": forms.Textarea(),
        },
    }


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    """Админ для модели Allergy"""

    list_display = ["name", "updated_at", "created_at"]


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    """Админ для модели Disease"""

    list_display = ["name", "updated_at", "created_at"]


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ["id", "user_info", "text", "is_visible"]
    list_display_links = ["id", "user_info"]
    formfield_overrides = {
        models.CharField: {
            "widget": forms.Textarea(),
        },
    }

    @admin.display(description="Пользователь")
    def user_info(self, obj):
        return obj.user_info
