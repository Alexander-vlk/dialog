from rest_framework import serializers

from constants import DATE_FORMAT


class DateFilterRequestSerializer(serializers.Serializer):
    """Сериализатор запроса по фильтру по дате"""

    date_start = serializers.DateField(help_text='Дата начала', format=DATE_FORMAT, required=False)
    date_end = serializers.DateField(help_text='Дата окончания', format=DATE_FORMAT, required=False)

    def validate(self, attrs):
        """Проверить параметры"""
        date_start = attrs.get('date_start')
        date_end = attrs.get('date_end')

        if (date_start and not date_end) or (date_end and not date_start):
            raise serializers.ValidationError(
                'Должны быть переданы либо оба параметра date_start и date_end, либо ни одного',
            )

        return attrs
