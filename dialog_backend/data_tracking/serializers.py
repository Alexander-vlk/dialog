from datetime import date, timedelta

from django.contrib.auth.models import User
from django.db.models import Avg
from django.utils import timezone
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from data_tracking.models import (
    BodyTemperature,
    DailyLog,
    Glucose,
    MonthlyLog,
    Pressure,
    WeeklyLog,
)
from data_tracking.templateviews import daily_log


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


class WeeklyLogSerializer(serializers.ModelSerializer):
    """Сериализатор модели WeeklyLog"""

    avg_data = serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model = WeeklyLog
        fields = (
            'weight',
            'bmi',
            'ketones',
            'avg_data',
        )

    def get_avg_data(self, obj):
        user = self.context.get('user')
        return (
            DailyLog.objects.filter(weekly_log=obj, user=user)
            .aggregate(
                avg_calories=Avg('calories_count'),
                avg_proteins=Avg('proteins_count'),
                avg_fats=Avg('fats_count'),
                avg_carbs=Avg('carbs_count'),
            )
        )

    def create(self, validated_data):
        user = self.context['request'].user
        week_start = date.today()
        week_end = week_start + timedelta(days=7)
        if user.is_authenticated:
            return WeeklyLog.objects.create(user=user, date=week_start, **validated_data)

        return WeeklyLog.objects.create(week_start=week_start, week_end=week_end,**validated_data)


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


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Return data example',
            description='Return temperature and creation date (format: HH:MM)',
            summary='Data for plots',
            value={
                'created_at': '10:00',
                'temperature': 36.6,
            },
        ),
    ],
    many=True,
)
class BodyTemperatureSerializer(serializers.ModelSerializer):
    """Сериализатор модели BodyTemperature"""

    created_at = serializers.DateTimeField(format='%H:%M', required=False, read_only=True)

    class Meta:
        model = BodyTemperature
        fields = (
            'created_at',
            'temperature',
        )

    def create(self, validated_data):
        user = self.context.get('user')

        if not user:
            return BodyTemperature.objects.create(
                **validated_data,
            )

        daily_log = DailyLog.objects.filter(user=user, date=timezone.now()).first()
        if not daily_log:
            BodyTemperature.objects.create(
                user=user,
                **validated_data,
            )

        return BodyTemperature.objects.create(
            user=user,
            daily_log=daily_log,
            **validated_data,
        )


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Return data example',
            description='Two fields: creation date and glucose level, need for plot creation',
            summary='Data for plots',
            value={
                'created_at': '23:00',
                'level': 3.4,
            },
        ),
    ],
    many=True,
)
class GlucoseSerializer(serializers.ModelSerializer):
    """Сериализатор модели Glucose"""

    created_at = serializers.DateTimeField(format='%H:%M (%d.%m)', required=False, read_only=True)

    class Meta:
        model = Glucose
        fields = (
            'created_at',
            'level',
        )

    def create(self, validated_data):
        user = self.context.get('user')
        if not user:
            return Glucose.objects.create(**validated_data)

        daily_log = DailyLog.objects.filter(user=user, date=timezone.now()).first()
        if not daily_log:
            return Glucose.objects.create(user=user, **validated_data)

        return Glucose.objects.create(user=user, daily_log=daily_log, **validated_data)


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Return data example',
            description='Two fields: creation date, systolic and diastolic pressure',
            summary='Data for plot',
            value={
                'created_at': '23:00',
                'systolic': 120,
                'diastolic': 80,
            }
        )
    ],
    many=True,
)
class PressureSerializer(serializers.ModelSerializer):
    """Сериализатор модели Pressure"""

    created_at = serializers.DateTimeField(format='%H:%M (%d.%m)', required=False, read_only=True)

    class Meta:
        model = Pressure
        fields = (
            'created_at',
            'systolic',
            'diastolic',
        )

    def create(self, validated_data):
        user = self.context.get('user')
        if not user:
            return Pressure.objects.create(**validated_data)

        daily_log = DailyLog.objects.filter(user=user, date=timezone.now()).first()
        if not daily_log:
            return Pressure.objects.create(user=user, **validated_data)

        return Pressure.objects.create(user=user, daily_log=daily_log, **validated_data)


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример возвращаемых данных',
            value=[
                {
                    'calories': 2100,
                    'date': '12.04',
                },
                {
                    'calories': 2200,
                    'date': '13.04',
                },
            ]
        )
    ]
)
class CaloriesSerializer(serializers.Serializer):
    """Сериализатор калорий"""

    calories_per_day = serializers.SerializerMethodField()

    def get_calories_per_day(self, weekly_log: WeeklyLog):
        """Геттер калорий за день"""
        user = self.context.get('user')

        daily_logs_in_week = (
            DailyLog.objects.filter(user=user, weekly_log=weekly_log)
            .values('date', 'calories_count')
            .order_by('date')
        )

        return [
            {
                'calories': daily_log_in_week.get('calories_count'),
                'date': daily_log_in_week.get('date').strftime('%d.%m'),
            }
            for daily_log_in_week in daily_logs_in_week
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'level': 3.0,
                    'date': '12.04',
                },
                {
                    'level': 3.5,
                    'date': '13.04',
                },
            ],
        ),
    ],
)
class AverageGlucoseSerializer(serializers.Serializer):
    """Сериализатор для получения данных о средней глюкозе за период"""

    average_glucose_per_day = serializers.SerializerMethodField()

    def _get_daily_logs(self, weekly_log: WeeklyLog):
        """Геттер получения дневного отчета"""
        user = self.context.get('user')

        return DailyLog.objects.filter(user=user, weekly_log=weekly_log).order_by('date')

    def get_average_glucose_per_day(self, weekly_log: WeeklyLog):
        """Геттер получения среднего уровня глюкозы за каждый день в течение недели"""
        daily_logs = self._get_daily_logs(weekly_log).annotate(avg_glucose_level=Avg('glucoses__level'))

        result = []
        for log in daily_logs:
            result.append({
                'level': log.avg_glucose_level,
                'date': log.date.strftime('%d.%m'),
            })

        return result
