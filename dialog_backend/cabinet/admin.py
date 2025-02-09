from django.contrib import admin

from cabinet.models import Allergy, Disease, UserProfile


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    """Админ для модели Allergy"""

    list_display = ['name', 'updated_at', 'created_at']


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    """Админ для модели Disease"""

    list_display = ['name', 'updated_at', 'created_at']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Админ для модели UserProfile"""
    
    list_display = ['user__username', 'gender', 'diabetes_type', 'updated_at']
    raw_id_fields = ['user']
