from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Успешный ответ',
            value={
                'calories_count': 0,
                'proteins_count': 0,
                'fats_count': 0,
                'carbs_count': 0,
                'mood': 3,
                'health_ids': [],
                'physical_activity': '',
                'additional_info': '',
                'date': '2025-09-19',
            },
        ),
    ],
)
class DailyLogRequestSerializer(serializers.Serializer):
    """Request serializer для DailyLog"""

    user_id = serializers.IntegerField(
        help_text='ID пользователя', allow_null=True, required=False
    )
    weekly_log_id = serializers.IntegerField(
        help_text='ID недельного отчета',
        allow_null=True,
        required=False,
    )
    calories_count = serializers.IntegerField(
        help_text='Количество калорий', min_value=0
    )
    proteins_count = serializers.IntegerField(
        help_text='Количество белков', min_value=0
    )
    fats_count = serializers.IntegerField(help_text='Количество жиров', min_value=0)
    carbs_count = serializers.IntegerField(
        help_text='Количество углеводов', min_value=0
    )
    mood = serializers.IntegerField(help_text='Настроение', min_value=1, max_value=5)
    health_ids = serializers.ListField(
        help_text='ID статусов самочувствия',
        child=serializers.IntegerField(),
        allow_empty=True,
    )
    physical_activity = serializers.CharField(
        help_text='Физическая активность',
        max_length=2000,
        allow_blank=True,
    )
    additional_info = serializers.CharField(
        help_text='Дополнительная информация',
        max_length=2000,
        allow_blank=True,
    )
    date = serializers.DateField(help_text='Дата замера', allow_null=True)
