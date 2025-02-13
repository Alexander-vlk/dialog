from rest_framework import serializers

from cabinet.models import Allergy, Disease, UserProfile


class AllergySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Allergy"""

    class Meta:
        model = Allergy
        fields = ('name',)

    def create(self, validated_data):
        allergy = super().create(validated_data)
        user = self.context['request'].user
        if user.is_authenticated:
            allergy.users.add(user)
        allergy.save()
        return allergy


class DiseaseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Disease"""

    class Meta:
        model = Disease
        fields = ('name',)

    def create(self, validated_data):
        disease = super().create(validated_data)
        user = self.context['request'].user
        if user.is_authenticated:
            disease.users.add(user)
        disease.save()
        return disease


class UserProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для модели UserProfile"""

    class Meta:
        model = UserProfile
        fields = (
            'patronymic_name',
            'gender',
            'birth_date',
            'diabetes_type',
            'diabetes_type',
            'diagnosis_date',
            'treatment_type',
            'phone_number',
        )

    def create(self, validated_data):
        user_profile = super().create(validated_data)
        user = self.context['request'].user
        if user.is_authenticated:
            user_profile.user = user
        user_profile.save()
        return user_profile
