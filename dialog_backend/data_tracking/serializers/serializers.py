from rest_framework import serializers

from data_tracking.models import (
    Temperature,
    Glucose,
    Hemoglobin,
    Mood,
    Cholesterol,
    LipidProfile,
    Microalbuminuria,
    Weight,
    Ketones,
    PhysicalActivity,
    Note,
    Meal,
)


class MoodSerializer(serializers.ModelSerializer):
    """Сериализатор для Mood"""

    class Meta:
        model = Mood
        fields = '__all__'


class TemperatureSerializer(serializers.ModelSerializer):
    """Сериализатор для Temperature"""

    class Meta:
        model = Temperature
        fields = '__all__'


class GlucoseSerializer(serializers.ModelSerializer):
    """Сериализатор для Glucose"""

    class Meta:
        model = Glucose
        fields = '__all__'


class HemoglobinSerializer(serializers.ModelSerializer):
    """Сериализатор для Hemoglobin"""

    class Meta:
        model = Hemoglobin
        fields = '__all__'


class CholesterolSerializer(serializers.ModelSerializer):
    """Сериализатор для Cholesterol"""

    class Meta:
        model = Cholesterol
        fields = '__all__'


class LipidProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для LipidProfile"""

    class Meta:
        model = LipidProfile
        fields = '__all__'


class MicroalbuminuriaSerializer(serializers.ModelSerializer):
    """Сериализатор для Microalbuminuria"""

    class Meta:
        model = Microalbuminuria
        fields = '__all__'


class WeightSerializer(serializers.ModelSerializer):
    """Сериализатор для Weight"""

    class Meta:
        model = Weight
        fields = '__all__'


class KetonesSerializer(serializers.ModelSerializer):
    """Сериализатор для Ketones"""

    class Meta:
        model = Ketones
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    """Сериализатор для Meal"""

    class Meta:
        model = Meal
        fields = '__all__'


class PhysicalActivitySerializer(serializers.ModelSerializer):
    """Сериализатор для PhysicalActivity"""

    class Meta:
        model = PhysicalActivity
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    """Сериализатор для Note"""

    class Meta:
        model = Note
        fields = '__all__'
