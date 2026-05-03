from django.contrib import admin

from cabinet.models import (
    Disease,
)


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    """Админ для Disease"""

    list_display = ['name']
