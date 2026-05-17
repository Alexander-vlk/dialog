from datetime import timedelta

from django.utils import timezone
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


class RecentDateTimeMixin:
    recent_datetime_fields: tuple[str, ...] = ()

    def validate(self, attrs):
        attrs = super().validate(attrs)
        min_datetime = timezone.now() - timedelta(days=14)
        max_datetime = timezone.now() + timedelta(days=14)

        for field_name in self.recent_datetime_fields:
            value = attrs.get(field_name)
            if value is None:
                continue
            if value < min_datetime or value > max_datetime:
                raise serializers.ValidationError({
                    field_name: 'Время должно быть в пределах последних 14 дней.'
                })

        return attrs


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


class TemperatureSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для Temperature"""

    class Meta:
        model = Temperature
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class PressureSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для Pressure"""

    class Meta:
        model = Pressure
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class GlucoseSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для Glucose"""

    class Meta:
        model = Glucose
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class HemoglobinSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для Hemoglobin"""

    class Meta:
        model = Hemoglobin
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class CholesterolSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для Cholesterol"""

    class Meta:
        model = Cholesterol
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class LipidProfileSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для LipidProfile"""

    class Meta:
        model = LipidProfile
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class MicroalbuminuriaSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для Microalbuminuria"""

    class Meta:
        model = Microalbuminuria
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class WeightSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для Weight"""

    class Meta:
        model = Weight
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class KetonesSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для Ketones"""

    class Meta:
        model = Ketones
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class MealSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для Meal"""

    class Meta:
        model = Meal
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('eaten_at',)


class PhysicalActivitySerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для PhysicalActivity"""

    class Meta:
        model = PhysicalActivity
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class NoteSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для Note"""

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class MoodAppUserSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для связки настроения и пользователя"""

    class Meta:
        model = MoodAppUser
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class HealthAppUserSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    """Сериализатор для связки самочувствия и пользователя"""

    class Meta:
        model = HealthAppUser
        fields = '__all__'
        read_only_fields = ['user']
    recent_datetime_fields = ('measured_at',)


class MedicationSerializer(serializers.ModelSerializer):
    """Сериализатор справочника препаратов"""

    class Meta:
        model = Medication
        fields = ['id', 'name', 'type', 'created_at', 'updated_at']


class MedicationTakeSerializer(RecentDateTimeMixin, serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    medication = MedicationSerializer(read_only=True)
    medication_id = serializers.PrimaryKeyRelatedField(
        queryset=Medication.objects.all(),
        source='medication',
        write_only=True,
    )

    class Meta:
        model = MedicationTake
        fields = [
            'id',
            'user',
            'medication',
            'medication_id',
            'taken_at',
            'dose',
            'comment',
            'created_at',
            'updated_at',
        ]

    recent_datetime_fields = ('taken_at',)
