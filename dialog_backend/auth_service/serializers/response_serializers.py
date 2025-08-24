from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

from rest_framework import serializers

from constants import GENDER_CHOICES, TREATMENTS_TYPE_CHOICES


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            "Пример ответа от сервера",
            description="Базовый ответ",
            value=[
                {
                    "id": "1",
                    "username": "testov",
                    "email": "test@test.com",
                    "last_name": "Тестов",
                    "first_name": "Тест",
                    "patronymic_name": "Тестович",
                    "image_url": "https://dialog.com/static/testov/profile.png",
                    "gender": "Мужской",
                    "birth_date": "2000-10-10",
                    "diabetes_type": "1-го типа",
                    "diagnosis_date": "2019-10-10",
                    "treatment_type": "Инсулинотерапия",
                    "phone_number": "79180001122",
                },
            ],
        ),
    ],
)
class AppUserResponseSerializer(serializers.Serializer):
    """Диализатор модели AppUser"""

    id = serializers.IntegerField(help_text="ID пользователя")
    username = serializers.CharField(help_text="Никнейм", max_length=150)
    first_name = serializers.CharField(help_text="Имя", max_length=150)
    last_name = serializers.CharField(help_text="Фамилия", max_length=150)
    patronymic_name = serializers.CharField(
        help_text="Отчество", max_length=150, allow_blank=True
    )
    email = serializers.EmailField(help_text="Email", allow_blank=True)
    phone_number = serializers.CharField(help_text="Номер телефона", allow_blank=True)
    image_url = serializers.CharField(help_text="URL изображения", allow_blank=True)
    gender = serializers.ChoiceField(help_text="Пол", choices=GENDER_CHOICES)
    birth_date = serializers.DateField(help_text="Дата рождения")
    diagnosis_date = serializers.DateField(help_text="Дата постановки диагноза")
    treatment_type = serializers.ChoiceField(
        help_text="Тип лечения", choices=TREATMENTS_TYPE_CHOICES, allow_blank=True
    )


class AccessTokenResponseSerializer(serializers.Serializer):
    """Сериализатор для access_token"""

    access = serializers.CharField(max_length=1000, help_text="Access-токен")
