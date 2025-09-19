from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from data_tracking.models import DailyLog


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Успешный ответ',
            value={
                'id': 18,
                'created_at': '2025-09-19T19:56:24.719694+03:00',
                'updated_at': '2025-09-19T19:56:24.719695+03:00',
                'calories_count': 0,
                'proteins_count': 0,
                'fats_count': 0,
                'carbs_count': 0,
                'mood': 3,
                'physical_activity': '',
                'additional_info': '',
                'date': '2025-09-19',
                'user': 1,
                'weekly_log': 3,
                'health': [],
            }
        ),
    ],
)
class DailyLogResponseSerializer(serializers.ModelSerializer):
    """Сериализатор модели DailyLog"""

    class Meta:
        model = DailyLog
        fields = '__all__'
