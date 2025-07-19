from django.core.exceptions import ValidationError

from constants import NO_DIABETES, NOT_SET


def validate_healthy_user_has_no_treatment_type(user):
    """Проверяет, что пользователь не имеет типа лечения, если он здоров"""
    if user.diabetes_type == NO_DIABETES and user.treatment_type != NOT_SET:
        raise ValidationError('Здоровый пользователь не может указать тип лечения')
