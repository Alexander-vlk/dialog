from datetime import date

from django.core.exceptions import ValidationError


def validate_not_future_date(validate_date):
    """Проверяет, что дата не в будущем"""
    if validate_date > date.today():
        raise ValidationError('Дата не может быть больше текущей')


def validate_positive_float(validate_number: float):
    """Проверяет, что число неотрицательное"""
    if validate_number < 0:
        raise ValidationError('Данный показатель не может быть отрицательным')


def validate_length(validate_text):
    """Проверяет длину текста"""
    if len(validate_text) < 100:
        raise ValidationError('Текст не может быть короче 100 символов')
