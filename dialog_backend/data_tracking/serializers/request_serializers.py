from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from constants import DATE_FORMAT
from data_tracking.constants import AvailableIndicators


class DateFilterRequestSerializer(serializers.Serializer):
    """Сериализатор запроса по фильтру по дате"""

    date_start = serializers.DateField(help_text='Дата начала', format=DATE_FORMAT)
    date_end = serializers.DateField(help_text='Дата окончания', format=DATE_FORMAT)

    def validate(self, attrs):
        """Проверить параметры"""
        date_start = attrs['date_start']
        date_end = attrs['date_end']
        if date_start > date_end:
            raise serializers.ValidationError('Параметр date_start не может быть больше date_end')

        return attrs


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Базовый ответ',
            value={
                'indicators': [
                    'glucose',
                    'hemoglobin',
                    'meal',
                ],
            },
        ),
    ],
)
class ReportRequestSerializer(serializers.Serializer):
    """Сериализатор запроса для отчетов"""

    indicators = serializers.ListField(
        help_text='Показатели',
        child=serializers.ChoiceField(choices=AvailableIndicators.ALL_CHOICES)
    )
