from datetime import date, timedelta

from rest_framework import serializers

from data_tracking.models import (
    BodyTemperature,
    DailyLog,
    Glucose,
    MonthlyLog,
    Pressure,
    WeeklyLog,
)


class BodyTemperatureSerializer(serializers.ModelSerializer):
    """Сериализатор модели BodyTemperature"""

    class Meta:
        model = BodyTemperature
        fields = (
            'temperature',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            return BodyTemperature.objects.create(user=user, **validated_data)


class DailyLogSerializer(serializers.ModelSerializer):
    """Сериализатор модели DailyLog"""

    class Meta:
        model = DailyLog
        fields = (
            'calories_count',
            'proteins_count',
            'fats_count',
            'carbs_count',
            'general_health',
            'physical_activity',
            'additional_info',
        )

    def validate_date(self, value):
        user = self.context['request'].user
        if user.is_authenticated and DailyLog.objects.filter(user=user, date=value).exists():
            raise serializers.ValidationError('Дневной отчет для этого дня уже существует')
        if value > date.today():
            raise serializers.ValidationError('Нельзя создать дневной отчет для еще не наступившего дня')

        return value

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            return DailyLog.objects.create(
                user=user,
                date=date.today(),
                **validated_data,
            )


class GlucoseSerializer(serializers.ModelSerializer):
    """Сериализатор модели Glucose"""

    class Meta:
        model = Glucose
        fields = (
            'level',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            return Glucose.objects.create(user=user, **validated_data)


class MonthlyLogSerializer(serializers.ModelSerializer):
    """Сериализатор модели MonthlyLog"""

    class Meta:
        model = MonthlyLog
        fields = (
            'hemoglobin',
            'cholesterol',
            'lipid_profile',
            'microalbuminuria',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            return MonthlyLog.objects.create(user=user, **validated_data)


class PressureSerializer(serializers.ModelSerializer):
    """Сериализатор модели Pressure"""

    created_at = serializers.DateTimeField(format='%H:%M')

    class Meta:
        model = Pressure
        fields = (
            'created_at',
            'systolic',
            'diastolic',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            return Pressure.objects.create(user=user, **validated_data)


class WeeklyLogSerializer(serializers.ModelSerializer):
    """Сериализатор модели WeeklyLog"""

    class Meta:
        model = WeeklyLog
        fields = (
            'weight',
            'bmi',
            'ketones',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        week_start = date.today()
        week_end = week_start + timedelta(days=7)
        if user.is_authenticated:
            return WeeklyLog.objects.create(user=user, date=week_start, **validated_data)

        return WeeklyLog.objects.create(week_start=week_start, week_end=week_end,**validated_data)
