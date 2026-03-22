from rest_framework import serializers

from cabinet.models import DiabetesType, TreatmentType, Disease


class DiabetesTypeSerializer(serializers.ModelSerializer):
    """Сериализатор для типов диабета"""

    class Meta:
        model = DiabetesType
        fields = '__all__'


class TreatmentTypeSerializer(serializers.ModelSerializer):
    """Сериализатор дял типов лечения"""

    class Meta:
        model = TreatmentType
        fields = '__all__'


class DiseaseSerializer(serializers.ModelSerializer):
    """Сериализатор для сопутствующих заболеваний"""

    class Meta:
        model = Disease
        fields = '__all__'
