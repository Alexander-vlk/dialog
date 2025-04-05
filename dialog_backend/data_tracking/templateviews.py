from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST, require_http_methods, require_GET

from data_tracking.forms import GlucoseForm, BodyTemperatureForm, PressureForm, DailyLogForm
from data_tracking.models import DailyLog, Glucose


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


@require_GET
def get_glucose_for_plot(request):
    """Получение информации для графика"""

    glucose_data = Glucose.objects.filter(
        user=request.user, daily_log__date=timezone.now()
    ).values_list('level', 'created_at')

    data, labels = zip(*glucose_data)

    return JsonResponse({
        'labels': [label.strftime('%H:%M') for label in labels],
        'data': data,
    })



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


@login_required
@require_http_methods(['GET', 'POST'])
def daily_log(request):
    """View для обработки ежедневного отчета"""
    daily_log_instance = DailyLog.objects.get(user=request.user, date=timezone.now())
    if request.method == "GET":
        form = DailyLogForm(instance=daily_log_instance)

        context = {
            'form': form,
        }

        template_name = 'daily_log.html'

        return render(request, template_name, context)

    form = DailyLogForm(request.POST, instance=daily_log_instance)

    if not form.is_valid():
        return HttpResponseBadRequest()

    form.save()

    cabinet_url = reverse('cabinet')
    return redirect(f'{cabinet_url}?filled_daily_log=true')
