from django.contrib.auth.password_validation import (
    validate_password as django_validate_password,
)
from rest_framework import serializers

from auth_service.models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели AppUser"""

    password_repeat = serializers.CharField(help_text='Пароль (еще раз)', required=False)

    class Meta:
        model = AppUser
        fields = '__all__'
        read_only_fields = [
            'date_joined',
            'groups',
            'user_permissions',
            'is_staff',
            'is_active',
            'is_superuser',
            'last_login',
        ]

    def validate_password(self, password):
        """Проверить пароль"""
        django_validate_password(password)
        return password

    def validate(self, attrs):
        """Проверить данные"""
        password_repeat = attrs.pop('password_repeat')
        if self.context.get('is_register'):
            if not password_repeat:
                raise serializers.ValidationError('При регистрации поле password_repeat обязательно')

            if attrs['password'] != password_repeat:
                raise serializers.ValidationError('Пароли не совпадают')

        return attrs

    def create(self, validated_data):
        """Создать пользователя"""
        diseases = validated_data.pop('diseases')
        new_user = AppUser.objects.create_user(**validated_data)
        new_user.diseases.set(diseases)
        return new_user
