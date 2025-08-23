import datetime

from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from auth_service.models import AppUser


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример',
            value={
                'username': 'test',
                'password1': '1234',
                'password2': '1234',
                'first_name': 'test',
                'last_name': 'test',
                'patronymic_name': 'test',
                'phone_number': '70000000000',
                'email': 'test@test.com',
                'gender': 'M',
                'birthday': '2000-10-01',
                'diabetes_type': '1',
                'treatments_type': '1',
                'profile_image': None,
                'remember': True,
                'agreed_with_privacy': True,
            },
            request_only=True,
        )
    ]
)
class UserRegistrationRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса для регистрации пользователя"""

    remember = serializers.BooleanField(help_text='Запомнить меня')
    agreed_with_privacy = serializers.BooleanField(help_text='Согласен с политикой конфиденциальности')

    class Meta:
        model = AppUser
        fields = '__all__'

    def validate_birthday(self, birthday):
        """Проверить дату рождения"""
        if birthday <= datetime.date(1900, 1, 1):
            raise serializers.ValidationError('День рождения не может быть меньше 1900 года')

        if birthday > datetime.date.today():
            raise serializers.ValidationError('День рождения не может быть в будущем')

        return birthday

    def validate_diagnosis_date(self, diagnosis_date):
        """Проверить дату постановки диагноза"""
        if diagnosis_date <= datetime.date(1900, 1, 1):
            raise serializers.ValidationError('Дата постановки диагноза не может быть меньше 1900 года')

        if diagnosis_date > datetime.date.today():
            raise serializers.ValidationError('Дата постановки диагноза не может быть в будущем')

        return diagnosis_date

    def validate_agreed_with_privacy(self, agreed_with_privacy):
        """Проверить agreed_with_privacy"""
        if not agreed_with_privacy:
            raise serializers.ValidationError('Пользователь не согласен с политикой конфиденциальности')

        return agreed_with_privacy

    def validate(self, obj):
        """Проверить все поля"""
        if obj.birthday <= obj.diagnosis_date:
            raise serializers.ValidationError('Дата постановки диагноза не может быть меньше даты рождения')

        if not obj.diabetes_type and (obj.diagnosis_date or obj.treatment_type):
            raise serializers.ValidationError('Тип лечения не может быть установлен, если Вы не болеете диабетом')

        return obj
