from rest_framework import serializers

from constants import DATE_FORMAT


class ReportResponseSerializer(serializers.Serializer):
    """Сериализатор ответа с данными отчета"""

    class AggregatedMetricSerializer(serializers.Serializer):
        """Сериализатор собранных метрик"""

        total = serializers.IntegerField(help_text='Общее кол-во записей')
        average = serializers.FloatField(help_text='Среднее значение')
        median = serializers.FloatField(help_text='Медианное значение')
        min = serializers.DictField(help_text='Объект с минимальным показателем', allow_null=True)
        max = serializers.DictField(help_text='Объект с максимальным показателем', allow_null=True)

    date_start = serializers.DateField(help_text='Дата начала', format=DATE_FORMAT)
    date_end = serializers.DateField(help_text='Дата окончания', format=DATE_FORMAT)
    aggregated_values = serializers.DictField(
        help_text='Собранные данные',
        child=AggregatedMetricSerializer(),
    )
