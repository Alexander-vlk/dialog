from django import forms

from data_tracking.models import (
    DailyLog,
    WeeklyLog,
    MonthlyLog,
    Glucose,
    Pressure,
    BodyTemperature
)


class GlucoseForm(forms.ModelForm):
    """Форма для замеров глюкозы"""

    class Meta:
        model = Glucose
        fields = ('level',)


class PressureForm(forms.ModelForm):
    """Форма для замеров давления"""

    class Meta:
        model = Pressure
        fields = ('systolic', 'diastolic')


class BodyTemperatureForm(forms.ModelForm):
    """Форма для замеров температуры тела"""

    class Meta:
        model = BodyTemperature
        fields = ('temperature',)