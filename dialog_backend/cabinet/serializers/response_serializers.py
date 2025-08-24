from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from cabinet.models import Advantage, Rate, TreatmentType


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            "Пример ответа от сервера",
            description="Базовый ответ",
            value=[
                {
                    "title": "Преимущество 1",
                    "description": "Описание преимущества",
                    "image_url": "https://dialog.com/media/advantages/advantage1.png",
                    "order_num": 1,
                },
            ],
        ),
    ],
)
class AdvantageResponseSerializer(serializers.ModelSerializer):
    """Сериализатор модели Advantage"""

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Advantage
        fields = ("title", "description", "image_url", "order_num")

    def get_image_url(self, obj):
        """Получить url изображения"""
        return obj.image.url if obj.image else ""


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            "Пример ответа от сервера",
            description="Базовый ответ",
            value=[
                {
                    "user_info": "Тестина Тестова",
                    "text": "Текст отзыва",
                },
                {
                    "user_info": "Тестина",
                    "text": "Текст отзыва",
                },
            ],
        ),
        OpenApiExample(
            "Анонимный отзыв",
            description="Пример ответа от сервера, если отзыв оставлен анонимным пользователем",
            value=[
                {
                    "user_info": "Аноним",
                    "text": "Текст отзыва",
                },
            ],
        ),
    ],
)
class RateResponseSerializer(serializers.ModelSerializer):
    """Сериализатор модели Rate"""

    class Meta:
        model = Rate
        fields = ("user_info", "text")


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            "Базовый ответ",
            value=[
                {
                    "slug": "not_set",
                    "name": "Не указывать",
                },
                {
                    "slug": "insulin_therapy",
                    "name": "Инсулинотерапия",
                },
                {
                    "slug": "preparations",
                    "name": "Препараты",
                },
            ],
        ),
    ],
)
class TreatmentTypeResponseSerializer(serializers.ModelSerializer):
    """Сериализатор модели TreatmentType"""

    class Meta:
        model = TreatmentType
        fields = ['slug', 'name']
