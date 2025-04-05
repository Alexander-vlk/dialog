from django import forms

from constants import TEXT_INPUT_CLASS, SELECT_INPUT_CLASS, TEXTAREA_INPUT_CLASS
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


class DailyLogForm(forms.ModelForm):
    """Форма дневного отчета"""

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

        widgets = {
            'calories_count': forms.NumberInput(attrs={'class': TEXT_INPUT_CLASS}),
            'proteins_count': forms.NumberInput(attrs={'class': TEXT_INPUT_CLASS}),
            'fats_count': forms.NumberInput(attrs={'class': TEXT_INPUT_CLASS}),
            'carbs_count': forms.NumberInput(attrs={'class': TEXT_INPUT_CLASS}),
            'general_health': forms.Select(attrs={'class': SELECT_INPUT_CLASS}),
            'physical_activity': forms.Textarea(attrs={'class': TEXTAREA_INPUT_CLASS}),
            'additional_info': forms.Textarea(attrs={'class': TEXTAREA_INPUT_CLASS}),
        }
