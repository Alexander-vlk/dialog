from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_GET

from cabinet.forms import UserProfileEditForm
from cabinet.models import Rate, Advantage
from data_tracking.models import DailyLog, Glucose, Pressure, BodyTemperature, WeeklyLog


def index(request):
    """View для главной страницы"""
    context = {
        'rates': Rate.objects.filter(is_visible=True)[:4],
        'advantages': Advantage.objects.all(),
    }
    return render(request, 'cabinet/index.html', context)


@require_GET
@login_required
def get_daily_log_fill_status(request):
    """Получение статуса заполнения дневного отчета"""
    daily_log = get_object_or_404(DailyLog, user=request.user, date=timezone.now())

    return JsonResponse({'is_filled': daily_log.is_filled})


@require_GET
@login_required
def get_weekly_log_fill_status(request):
    """Возвращает статус заполнения недельного отчета"""

    weekly_log = get_object_or_404(
        WeeklyLog,
        user=request.user,
        week_start__lte=timezone.now(),
        week_end__gt=timezone.now(),
    )

    status = 'late'
    if weekly_log.week_end > timezone.now():
        status = 'early'
    elif weekly_log.week_end == timezone.now():
        status = 'in_time'

    return JsonResponse({
        'status': status,
        'is_filled': weekly_log.is_filled,
    })


@login_required
def cabinet(request):
    """View для страницы личного кабинета"""
    daily_log = DailyLog.objects.filter(user=request.user, date=timezone.now()).first()

    glucose_per_day_count = Glucose.objects.filter(daily_log=daily_log).count()
    pressure_per_day_count = Pressure.objects.filter(daily_log=daily_log).count()
    temperature_per_day_count = BodyTemperature.objects.filter(daily_log=daily_log).count()

    weekly_log = WeeklyLog.objects.filter(
        user=request.user,
        week_start__lte=timezone.now(),
        week_end__gt=timezone.now(),
    ).first()

    context = {
        'cabinet': request.user.userprofile,
        'daily_log': daily_log,
        'weekly_log': weekly_log,
        'glucose_per_day_count': glucose_per_day_count,
        'pressure_per_day_count': pressure_per_day_count,
        'temperature_per_day_count': temperature_per_day_count,
    }

    return render(request, 'cabinet/cabinet.html', context)


@require_http_methods(['GET', 'POST'])
@login_required
def edit_profile(request):
    """View редактирования профиля"""
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            request.user.username = form.cleaned_data['username']
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()

            cabinet_url = reverse('cabinet')
            return redirect(f'{cabinet_url}?success_edit_profile=true')

    form = UserProfileEditForm(instance=request.user.userprofile)

    template = 'cabinet/edit_profile.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

