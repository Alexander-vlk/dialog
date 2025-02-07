from datetime import date

from django.core.exceptions import ValidationError


def validate_not_future_date(validate_date):
    """Проверяет, что дата не в будущем"""
    if validate_date > date.today():
        raise ValidationError('Дата не может быть больше текущей')
