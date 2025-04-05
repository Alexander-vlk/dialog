from django.contrib import admin

from data_tracking.models import (
    MonthlyLog,
    WeeklyLog,
    DailyLog,
    BodyTemperature,
    Glucose,
    Pressure,
)


@admin.register(MonthlyLog)
class MonthlyLogAdmin(admin.ModelAdmin):
    """Админ для MonthlyLog"""

    list_display = ('user', 'created_at', 'month')
    raw_id_fields = ('user',)


@admin.register(WeeklyLog)
class WeeklyLogAdmin(admin.ModelAdmin):
    """Админ для WeeklyLog"""

    list_display = ('user', 'monthly_log', 'week_start', 'week_end', 'created_at')
    raw_id_fields = ('user', 'monthly_log')


@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    """Админ для модели DailyLog"""

    list_display = ('user', 'weekly_log', 'date')
    raw_id_fields = ('user', 'weekly_log')


@admin.register(BodyTemperature)
class BodyTemperatureAdmin(admin.ModelAdmin):
    """Админ для модели BodyTemperature"""

    list_display = ('user', 'daily_log', 'created_at')
    raw_id_fields = ('user', 'daily_log')


@admin.register(Glucose)
class GlucoseAdmin(admin.ModelAdmin):
    """Админ для модели Glucose"""

    list_display = ('user', 'daily_log', 'created_at')
    raw_id_fields = ('user', 'daily_log')


@admin.register(Pressure)
class PressureAdmin(admin.ModelAdmin):
    """Админ для модели Pressure"""

    list_display = ('user', 'daily_log', 'created_at')
    raw_id_fields = ('user', 'daily_log')
