import datetime

from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from auth_service.models import AppUser
from auth_service.validators.serializer_validators import drf_validate_password


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример',
            value={
                'username': 'test',
                'password': '1234',
                'repeat_password': '1234',
                'first_name': 'test',
                'last_name': 'test',
                'patronymic_name': 'test',
                'phone_number': '70000000000',
                'email': 'test@test.com',
                'gender': 'MALE',
                'birth_date': '2000-10-01',
                'diabetes_type': '1',
                'diagnosis_date': '2020-10-01',
                'treatment_type': 'not_set',
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

    repeat_password = serializers.CharField(
        write_only=True,
        required=True,
        max_length=128,
        help_text='Пароль (еще раз)'
    )

    remember = serializers.BooleanField(help_text='Запомнить меня')
    agreed_with_privacy = serializers.BooleanField(help_text='Согласен с политикой конфиденциальности')

    class Meta:
        model = AppUser
        fields = (
            'username',
            'password',
            'repeat_password',
            'first_name',
            'last_name',
            'patronymic_name',
            'phone_number',
            'email',
            'gender',
            'birth_date',
            'diabetes_type',
            'diagnosis_date',
            'treatment_type',
            'image',
            'remember',
            'agreed_with_privacy',
        )

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

    def validate(self, data):
        """Проверить все поля"""
        if data['birth_date'] > data['diagnosis_date']:
            raise serializers.ValidationError('Дата постановки диагноза не может быть меньше даты рождения')

        if not data['diabetes_type'] and (data['diagnosis_date'] or data['treatment_type']):
            raise serializers.ValidationError('Тип лечения не может быть установлен, если Вы не болеете диабетом')

        drf_validate_password(data['password'], data['repeat_password'])

        return data

    def create(self, validated_data):
        """Создать пользователя"""
        return AppUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            patronymic_name=validated_data['patronymic_name'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            gender=validated_data['gender'],
            birth_date=validated_data['birth_date'],
            diabetes_type=validated_data['diabetes_type'],
            diagnosis_date=validated_data['diagnosis_date'],
            treatment_type=validated_data['treatment_type'],
        )
