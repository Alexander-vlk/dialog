from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST, require_http_methods, require_GET
from django.views.generic import ListView

from data_tracking.forms import GlucoseForm, BodyTemperatureForm, PressureForm, DailyLogForm
from data_tracking.models import DailyLog, Glucose, Pressure


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
@require_GET
def get_glucose_for_plot(request):
    """Получение информации для графика"""
    glucose_data = Glucose.objects.filter(
        user=request.user, daily_log__date=timezone.now()
    ).values_list('level', 'created_at')

    data, labels = zip(*glucose_data)
    local_labels = [timezone.localtime(label).strftime('%H:%M') for label in labels]

    return JsonResponse({
        'labels': local_labels,
        'data': data,
    })


@login_required
@require_GET
def get_pressure_for_plot(request):
    """Получение информации о давлении для графика"""
    pressure_data = Pressure.objects.filter(
        user=request.user, daily_log__date=timezone.now()
    ).values_list('created_at', 'systolic', 'diastolic')

    labels, systolic, diastolic = zip(*pressure_data)
    local_labels = [timezone.localtime(label).strftime('%H:%M') for label in labels]

    return JsonResponse({
        'labels': local_labels,
        'systolic': systolic,
        'diastolic': diastolic,
    })


@login_required
@require_GET
def get_temperature_for_plot(request):
    """Получение данных о температуре для графика"""
    temperature_data = Glucose.objects.filter(
        user=request.user, daily_log__date=timezone.now()
    ).values_list('created_at', 'temperature')

    data, labels = zip(*temperature_data)
    local_labels = [timezone.localtime(label).strftime('%H:%M') for label in labels]

    return JsonResponse({
        'labels': local_labels,
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


class DailyLogListView(ListView):
    """Страница со списком дневных отчетов"""

    template_name = 'data_tracking/daily_log_list.html'
    context_object_name = 'daily_logs'
    paginate_by = 7

    def get_queryset(self):
        return DailyLog.objects.filter(user=self.request.user).annotate(
            glucose_count=Count('glucoses', distinct=True),
            pressure_count=Count('pressures', distinct=True),
            temperature_count=Count('body_temperatures', distinct=True),
            avg_glucose=Avg('glucoses__level', distinct=True),
            avg_temperature=Avg('body_temperatures__temperature', distinct=True),
            avg_systolic=Avg('pressures__systolic', distinct=True),
            avg_diastolic=Avg('pressures__diastolic', distinct=True),
        ).order_by('-date')
