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
    MoodAppUser,
    Health,
    HealthAppUser, Pressure, Medication, MedicationTake,
)


class MoodSerializer(serializers.ModelSerializer):
    """Сериализатор для Mood"""

    class Meta:
        model = Mood
        fields = '__all__'


class HealthSerializer(serializers.ModelSerializer):
    """Сериализатор для Health"""

    class Meta:
        model = Health
        fields = '__all__'


class TemperatureSerializer(serializers.ModelSerializer):
    """Сериализатор для Temperature"""

    class Meta:
        model = Temperature
        fields = '__all__'
        read_only_fields = ['user']


class PressureSerializer(serializers.ModelSerializer):
    """Сериализатор для Pressure"""

    class Meta:
        model = Pressure
        fields = '__all__'
        read_only_fields = ['user']


class GlucoseSerializer(serializers.ModelSerializer):
    """Сериализатор для Glucose"""

    class Meta:
        model = Glucose
        fields = '__all__'
        read_only_fields = ['user']


class HemoglobinSerializer(serializers.ModelSerializer):
    """Сериализатор для Hemoglobin"""

    class Meta:
        model = Hemoglobin
        fields = '__all__'
        read_only_fields = ['user']


class CholesterolSerializer(serializers.ModelSerializer):
    """Сериализатор для Cholesterol"""

    class Meta:
        model = Cholesterol
        fields = '__all__'
        read_only_fields = ['user']


class LipidProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для LipidProfile"""

    class Meta:
        model = LipidProfile
        fields = '__all__'
        read_only_fields = ['user']


class MicroalbuminuriaSerializer(serializers.ModelSerializer):
    """Сериализатор для Microalbuminuria"""

    class Meta:
        model = Microalbuminuria
        fields = '__all__'
        read_only_fields = ['user']


class WeightSerializer(serializers.ModelSerializer):
    """Сериализатор для Weight"""

    class Meta:
        model = Weight
        fields = '__all__'
        read_only_fields = ['user']


class KetonesSerializer(serializers.ModelSerializer):
    """Сериализатор для Ketones"""

    class Meta:
        model = Ketones
        fields = '__all__'
        read_only_fields = ['user']


class MealSerializer(serializers.ModelSerializer):
    """Сериализатор для Meal"""

    class Meta:
        model = Meal
        fields = '__all__'
        read_only_fields = ['user']


class PhysicalActivitySerializer(serializers.ModelSerializer):
    """Сериализатор для PhysicalActivity"""

    class Meta:
        model = PhysicalActivity
        fields = '__all__'
        read_only_fields = ['user']


class NoteSerializer(serializers.ModelSerializer):
    """Сериализатор для Note"""

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['user']


class MoodAppUserSerializer(serializers.ModelSerializer):
    """Сериализатор для связки настроения и пользователя"""

    class Meta:
        model = MoodAppUser
        fields = '__all__'
        read_only_fields = ['user']


class HealthAppUserSerializer(serializers.ModelSerializer):
    """Сериализатор для связки самочувствия и пользователя"""

    class Meta:
        model = HealthAppUser
        fields = '__all__'
        read_only_fields = ['user']


class MedicationSerializer(serializers.ModelSerializer):
    """Сериализатор справочника препаратов"""

    class Meta:
        model = Medication
        fields = ['id', 'name', 'type', 'created_at', 'updated_at']


class MedicationTakeSerializer(serializers.ModelSerializer):
    """Сериализатор приема лекарства"""

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = MedicationTake
        fields = [
            'id',
            'user',
            'medication',
            'taken_at',
            'dose',
            'comment',
            'created_at',
            'updated_at',
        ]
