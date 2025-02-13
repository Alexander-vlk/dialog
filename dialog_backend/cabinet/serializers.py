from rest_framework import serializers

from cabinet.models import Allergy, Disease, UserProfile


class AllergySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Allergy"""

    class Meta:
        model = Allergy
        fields = ('name',)

    def create(self, validated_data):
        allergy = super().create(validated_data)
        allergy.users.add(self.context['request'].user)
        return allergy


class DiseaseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Disease"""

    class Meta:
        model = Disease
        fields = ('name',)

    def create(self, validated_data):
        disease = super().create(validated_data)
        disease.users.add(self.context['request'].user)
        return disease
