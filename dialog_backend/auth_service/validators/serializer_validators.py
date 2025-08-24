from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers


def drf_validate_password(password, password_repeat) -> None:
    """Проверить пароль"""
    if password != password_repeat:
        raise serializers.ValidationError("Пароли не совпадают")

    try:
        validate_password(password)
    except exceptions.ValidationError as django_validation_error:
        raise serializers.ValidationError(list(django_validation_error.messages))
