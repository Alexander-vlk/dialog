from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from constants import DATE_FORMAT


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Стандартный ответ',
            value={
                'date_start': '2020-10-10',
                'date_end': '2020-10-10',
                'aggregated_values': {
                    'glucose': {
                        'total': 2,
                        'average_values': {
                            'value': 1.5,
                        },
                        'median_values': {
                            'value': 1.5,
                        },
                        'min_value': {
                            'id': 1,
                            'value': 1,
                            'measured_at': '2026-03-07T15:20:44.695Z',
                            'created_at': '2026-03-07T15:20:44.695Z',
                            'updated_at': '2026-03-07T15:20:44.695Z',
                        },
                        'max_value': {
                            'id': 2,
                            'value': 2,
                            'measured_at': '2026-03-07T15:20:44.695Z',
                            'created_at': '2026-03-07T15:20:44.695Z',
                            'updated_at': '2026-03-07T15:20:44.695Z',
                        },
                    },
                    'pressure': {
                        'total': 2,
                        'average_values': {
                            'systolic': 105,
                            'diastolic': 155,
                        },
                        'median_values': {
                            'systolic': 105,
                            'diastolic': 155,
                        },
                        'min_value': {
                            'id': 1,
                            'systolic': 10,
                            'diastolic': 10,
                            'measured_at': '2026-03-07T15:20:44.695Z',
                            'created_at': '2026-03-07T15:20:44.695Z',
                            'updated_at': '2026-03-07T15:20:44.695Z',
                        },
                        'max_value': {
                            'id': 2,
                            'systolic': 200,
                            'diastolic': 300,
                            'measured_at': '2026-03-07T15:20:44.695Z',
                            'created_at': '2026-03-07T15:20:44.695Z',
                            'updated_at': '2026-03-07T15:20:44.695Z',
                        },
                    },
                    'meal': {
                        'total': 0,
                        'average_values': {
                            'calories': None,
                            'proteins': None,
                            'carbs': None,
                            'fats': None,
                        },
                        'median_values': {
                            'calories': None,
                            'proteins': None,
                            'carbs': None,
                            'fats': None,
                        },
                        'min_value': None,
                        'max_value': None,
                    },
                },
            },
        ),
    ]
)
class ReportResponseSerializer(serializers.Serializer):
    """Сериализатор ответа с данными отчета"""

    class AggregatedMetricSerializer(serializers.Serializer):
        """Сериализатор собранных метрик"""

        total = serializers.IntegerField(help_text='Общее кол-во записей', default=0)
        average_values = serializers.DictField(help_text='Средние значения', default=dict)
        median_values = serializers.DictField(help_text='Медианные значения', default=dict)
        min_value = serializers.DictField(help_text='Объект с минимальным показателем', allow_null=True, default=None)
        max_value = serializers.DictField(help_text='Объект с максимальным показателем', allow_null=True, default=None)

    date_start = serializers.DateField(help_text='Дата начала', format=DATE_FORMAT)
    date_end = serializers.DateField(help_text='Дата окончания', format=DATE_FORMAT)
    aggregated_values = serializers.DictField(
        help_text='Собранные данные',
        child=AggregatedMetricSerializer(),
    )
