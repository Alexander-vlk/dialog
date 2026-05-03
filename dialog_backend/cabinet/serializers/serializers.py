from rest_framework import serializers

from cabinet.models import Disease


class DiseaseSerializer(serializers.ModelSerializer):
    """Сериализатор для сопутствующих заболеваний"""

    class Meta:
        model = Disease
        fields = '__all__'
