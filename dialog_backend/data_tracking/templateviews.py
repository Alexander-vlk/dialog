from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_POST

from data_tracking.forms import GlucoseForm, BodyTemperatureForm, PressureForm
from data_tracking.models import DailyLog


@login_required
@require_POST
def glucose(request):
    """Сохранение замеров глюкозы"""
    form = GlucoseForm(request.POST)

    if not form.is_valid():
        return HttpResponseBadRequest()

    daily_log = DailyLog.objects.get(user=request.user, date=timezone.now())

    glucose_instance = form.save(commit=False)
    glucose_instance.user = request.user
    glucose_instance.daily_log = daily_log
    glucose_instance.save()

    return JsonResponse({'success': True})


@login_required
@require_POST
def pressure(request):
    """Сохранение замеров давления"""
    form = PressureForm(request.POST)

    if not form.is_valid():
        return HttpResponseBadRequest()

    daily_log = DailyLog.objects.get(user=request.user, date=timezone.now())

    pressure_instance = form.save(commit=False)
    pressure_instance.user = request.user
    pressure_instance.daily_log = daily_log
    pressure_instance.save()

    return JsonResponse({'success': True})


@login_required
@require_POST
def temperature(request):
    """Сохранение замеров температуры"""
    form = BodyTemperatureForm(request.POST)

    if not form.is_valid():
        return HttpResponseBadRequest()

    daily_log = DailyLog.objects.get(user=request.user, date=timezone.now())

    temperature_instance = form.save(commit=False)
    temperature_instance.user = request.user
    temperature_instance.daily_log = daily_log
    temperature_instance.save()

    return JsonResponse({'success': True})
