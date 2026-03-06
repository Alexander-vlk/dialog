from django.contrib import admin

from data_tracking.models import (
    Temperature,
    Glucose,
    Hemoglobin,
    Cholesterol,
    LipidProfile,
    Microalbuminuria,
    Weight,
    Ketones,
    Meal,
    PhysicalActivity,
    Note,
    Mood,
    MoodAppUser,
    Health,
    HealthAppUser,
)


@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    """Админ для модели Temperature"""

    list_display = ['user', 'measured_at']
    raw_id_fields = ['user']
    search_fields = ['user', 'measured_at']


@admin.register(Glucose)
class GlucoseAdmin(admin.ModelAdmin):
    """Админ для модели Glucose"""

    list_display = ['user', 'measured_at']
    raw_id_fields = ['user']
    search_fields = ['user', 'measured_at']


@admin.register(Hemoglobin)
class HemoglobinAdmin(admin.ModelAdmin):
    """Админ для модели Hemoglobin"""

    list_display = ['user', 'measured_at']
    raw_id_fields = ['user']
    search_fields = ['user', 'measured_at']


@admin.register(Cholesterol)
class CholesterolAdmin(admin.ModelAdmin):
    """Админ для модели Hemoglobin"""

    list_display = ['user', 'measured_at']
    raw_id_fields = ['user']
    search_fields = ['user', 'measured_at']


@admin.register(LipidProfile)
class LipidProfileAdmin(admin.ModelAdmin):
    """Админ для модели LipidProfile"""

    list_display = ['user', 'measured_at']
    raw_id_fields = ['user']
    search_fields = ['user', 'measured_at']


@admin.register(Microalbuminuria)
class MicroalbuminuriaAdmin(admin.ModelAdmin):
    """Админ для модели Microalbuminuria"""

    list_display = ['user', 'measured_at']
    raw_id_fields = ['user']
    search_fields = ['user', 'measured_at']


@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    """Админ для модели Weight"""

    list_display = ['user', 'measured_at']
    raw_id_fields = ['user']
    search_fields = ['user', 'measured_at']


@admin.register(Ketones)
class KetonesAdmin(admin.ModelAdmin):
    """Админ для модели Ketones"""

    list_display = ['user', 'measured_at']
    raw_id_fields = ['user']
    search_fields = ['user', 'measured_at']


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    """Админ для модели Meal"""

    list_display = ['user', 'eaten_at']
    raw_id_fields = ['user']
    search_fields = ['user', 'eaten_at']


@admin.register(PhysicalActivity)
class PhysicalActivityAdmin(admin.ModelAdmin):
    """Админ для модели PhysicalActivity"""

    list_display = ['user', 'measured_at']
    raw_id_fields = ['user']
    search_fields = ['user', 'measured_at']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Админ для модели Note"""

    list_display = ['user', 'measured_at']
    raw_id_fields = ['user']
    search_fields = ['user', 'measured_at']


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    """Админ для модели Mood"""

    list_display = ['name', 'text_color', 'background_color']
    search_fields = ['name', 'text_color', 'background_color']


@admin.register(MoodAppUser)
class MoodAppUserAdmin(admin.ModelAdmin):
    """Админ для модели MoodAppUser"""

    list_display = ['user', 'mood', 'measured_at']
    raw_id_fields = ['user', 'mood']
    search_fields = ['user', 'mood__name', 'measured_at']


@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    """Админ для модели Health"""

    list_display = ['name', 'text_color', 'background_color']
    search_fields = ['name', 'text_color', 'background_color']


@admin.register(HealthAppUser)
class HealthAppUserAdmin(admin.ModelAdmin):
    """Админ для модели HealthAppUser"""

    list_display = ['user', 'health', 'measured_at']
    raw_id_fields = ['user', 'health']
    search_fields = ['user', 'health__name', 'measured_at']
