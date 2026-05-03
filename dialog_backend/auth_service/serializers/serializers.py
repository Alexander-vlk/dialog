from django.contrib.auth.password_validation import (
    validate_password as django_validate_password,
)
from rest_framework import serializers

from auth_service.models import AppUser


class RegisterUserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели AppUser"""

    password_repeat = serializers.CharField(help_text='Пароль (еще раз)')
    access_token = serializers.SerializerMethodField(help_text='Access Token')

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

    def get_access_token(self, obj: AppUser):
        """Получить access_token из контекста сериализатора"""
        return  self.context['access_token']

    @staticmethod
    def validate_password(password):
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
        diseases = []
        if validated_data.get('diseases'):
            diseases = validated_data.pop('diseases')

        new_user = AppUser.objects.create_user(**validated_data)
        new_user.diseases.set(diseases)
        return new_user
