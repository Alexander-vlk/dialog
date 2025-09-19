from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Успешный ответ',
            value={
                'user_id': 18,
                'weekly_log_id': 0,
                'calories_count': 0,
                'proteins_count': 0,
                'fats_count': 0,
                'carbs_count': 0,
                'mood': 3,
                'health': [],
                'physical_activity': '',
                'additional_info': '',
                'date': '2025-09-19',
            },
        ),
    ],
)
class DailyLogRequestSerializer(serializers.Serializer):
    """Request serializer для DailyLog"""

    user_id = serializers.IntegerField(help_text='ID пользователя', allow_null=True)
    weekly_log_id = serializers.IntegerField(
        help_text='ID недельного отчета', allow_null=True,
    )
    calories_count = serializers.IntegerField(help_text='Количество калорий')
    proteins_count = serializers.IntegerField(help_text='Количество белков')
    fats_count = serializers.IntegerField(help_text='Количество жиров')
    carbs_count = serializers.IntegerField(help_text='Количество углеводов')
    mood = serializers.IntegerField(help_text='Настроение')
    health = serializers.ListField(
        help_text='ID статусов самочувствия',
        child=serializers.IntegerField(),
        allow_empty=True,
    )
    physical_activity = serializers.CharField(
        help_text='Физическая активность', max_length=2000, allow_blank=True,
    )
    additional_info = serializers.CharField(
        help_text='Дополнительная информация', max_length=2000, allow_blank=True,
    )
    date = serializers.DateField(help_text='Дата замера', allow_null=True)

    def validate_mood(self, mood):
        """Проверить mood, что значение находится между 1 и 5"""
        if mood not in range(1, 6):
            raise serializers.ValidationError(
                'mood can not be lower than 1 and higher than 5'
            )
