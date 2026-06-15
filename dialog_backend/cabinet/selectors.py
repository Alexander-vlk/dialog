from django.utils import timezone

from auth_service.models import AppUser
from data_tracking.models import Glucose, Temperature, Pressure, Hemoglobin, Cholesterol, LipidProfile, \
    Microalbuminuria, Weight, Ketones, Meal, PhysicalActivity, Note, Mood, MedicationTake, Health


def get_user_streak_data(user: AppUser) -> bool:
    """Получить данные об ударном режиме пользователя"""
    available_measure_models = [
        Temperature,
        Pressure,
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
        MedicationTake,
    ]
    return any(
        model.objects.filter(user=user, created_at__gt=timezone.now().date()).exists()
        for model in available_measure_models
    )
