from rest_framework import serializers

class UserStreakResponseSerializer(serializers.Serializer):
    """Сериализатор ответа хука получения ударного режима пользователя"""

    days_count = serializers.IntegerField(help_text='Количество дней ударного режима', min_value=0)
    is_active = serializers.BooleanField(help_text='Ударный режим активен')
