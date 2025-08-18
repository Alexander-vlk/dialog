import datetime

from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from constants import GENDER_CHOICES, TREATMENTS_TYPE_CHOICES, DIABETES_TYPE_CHOICES


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
class UserRegistrationRequestSerializer(serializers.Serializer):
    """Сериализатор запроса для регистрации пользователя"""

    username = serializers.CharField(help_text='Имя пользователя')
    password1 = serializers.CharField(help_text='Пароль')
    password2 = serializers.CharField(help_text='Пароль (еще раз)')

    first_name = serializers.CharField(help_text='Имя', max_length=50)
    last_name = serializers.CharField(help_text='Фамилия', max_length=50)
    patronymic_name = serializers.CharField(help_text='Отчество', max_length=50)

    phone_number = serializers.CharField(help_text='Номер телефона', max_length=13)
    email = serializers.EmailField(help_text='Email')
    gender = serializers.ChoiceField(help_text='Пол', choices=GENDER_CHOICES)
    birthday = serializers.DateField(help_text='Дата рождения')

    diabetes_type = serializers.ChoiceField(help_text='Тип диабета', choices=DIABETES_TYPE_CHOICES, allow_blank=True)
    diagnosis_date = serializers.DateField(help_text='Дата постановки диагноза', allow_null=True)
    treatment_type = serializers.ChoiceField(help_text='Тип лечения', choices=TREATMENTS_TYPE_CHOICES, allow_blank=True)

    profile_image = serializers.ImageField(help_text='Фото профиля', allow_null=True)

    remember = serializers.BooleanField(help_text='Запомнить меня')
    agreed_with_privacy = serializers.BooleanField(help_text='Согласен с политикой конфиденциальности')

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
