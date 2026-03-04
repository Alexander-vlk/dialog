from django.contrib import admin

from cabinet.models import (
    DiabetesType,
    Disease,
    TreatmentType,
)


@admin.register(DiabetesType)
class DiabetesTypeAdmin(admin.ModelAdmin):
    """Админ для Disease"""

    list_display = ['name']


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    """Админ для Disease"""

    list_display = ['name']


@admin.register(TreatmentType)
class TreatmentTypeAdmin(admin.ModelAdmin):
    """Админ для Disease"""

    list_display = ['name']
