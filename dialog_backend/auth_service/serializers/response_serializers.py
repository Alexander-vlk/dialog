from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

from rest_framework import serializers

from auth_service.models import AppUser
from constants import GENDER_CHOICES



@extend_schema_serializer(
    many=False,
    examples=[
        OpenApiExample(
            'Пример токена',
            value={
                'access_token': 'some_cool_key',
            },
        ),
    ],
)
class AccessTokenResponseSerializer(serializers.Serializer):
    """Сериализатор для access_token"""

    access_token = serializers.CharField(max_length=1000, help_text='Access-токен')


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': 3,
                    'access_token': 'test',
                    'created_at': '2026-05-03T19:20:46.007038+03:00',
                    'updated_at': '2026-05-03T19:20:46.007055+03:00',
                    'last_login': '2026-05-03T19:20:49.797297+03:00',
                    'is_superuser': True,
                    'username': 'admin',
                    'first_name': '',
                    'last_name': '',
                    'email': '',
                    'is_staff': False,
                    'is_active': False,
                    'date_joined': '2026-05-03T19:20:45.844119+03:00',
                    'image': '/media/images/stub.png',
                    'patronymic_name': '',
                    'gender': 'undefined',
                    'height': None,
                    'birth_date': None,
                    'diagnosis_date': None,
                    'phone_number': '',
                    'town': None,
                    'groups': [],
                    'user_permissions': [],
                    'moods': [],
                    'healths': [],
                    'diseases': [],
                },
            ],
        ),
    ],
)
class AppUserResponseSerializer(serializers.ModelSerializer):
    """Диализатор модели AppUser"""

    access_token = serializers.SerializerMethodField(help_text='Access Token')

    class Meta:
        model = AppUser
        exclude = ['password']

    def get_access_token(self, obj: AppUser):
        """Получить access_token из контекста сериализатора"""
        return  self.context['access_token']
