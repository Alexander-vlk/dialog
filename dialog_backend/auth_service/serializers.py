from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

from rest_framework.serializers import ModelSerializer


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'id': '1',
                    'username': 'testov',
                    'email': 'test@test.com',
                    'last_name': 'Тестов',
                    'first_name': 'Тест',
                },
            ],
        ),
    ],
)
class UserSerializer(ModelSerializer):
    """Сериализатор для модели User"""
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'last_name', 'first_name')
