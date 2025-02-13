from rest_framework import serializers

from cabinet.models import Allergy, Disease, UserProfile


class AllergySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Allergy"""

    class Meta:
        model = Allergy
        fields = ('name', )

    def create(self, validated_data):
        allergy = super().create(validated_data)
        allergy.users.add(self.context['request'].user)
        return allergy
