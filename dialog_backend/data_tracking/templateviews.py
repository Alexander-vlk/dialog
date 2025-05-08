from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from data_tracking.forms import DailyLogForm, WeeklyLogForm
from data_tracking.models import DailyLog, WeeklyLog, MonthlyLog


@login_required
@require_http_methods(['GET', 'POST'])
def weekly_log(request):
    """View для обработки еженедельного отчета"""
    weekly_log_instance = WeeklyLog.objects.get(
        user=request.user,
        week_start__lte=timezone.now(),
        week_end__gt=timezone.now(),
    )
    if request.method == "GET":
        form = WeeklyLogForm(instance=weekly_log_instance)

        context_data = {
            'form': form,
        }

        template_name = 'weekly_log.html'

        return render(request, template_name, context_data)

    form = WeeklyLogForm(request.POST, instance=weekly_log_instance)

    if not form.is_valid():
        return HttpResponseBadRequest()

    form.save()

    cabinet_url = reverse('cabinet')
    return redirect(f'{cabinet_url}?filled_weekly_log=true')


@login_required
@require_http_methods(['GET', 'POST'])
def daily_log(request):
    """View для обработки ежедневного отчета"""
    daily_log_instance = DailyLog.objects.get(user=request.user, date=timezone.now())
    if request.method == "GET":
        form = DailyLogForm(instance=daily_log_instance)

        context_data = {
            'form': form,
        }

        template_name = 'daily_log.html'

        return render(request, template_name, context_data)

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


class WeeklyLogListView(ListView):
    """Страница со списком еженедельных отчетов"""

    template_name = 'data_tracking/weekly_log_list.html'
    context_object_name = 'weekly_logs'
    paginate_by = 1

    def get_queryset(self):
        return (
            WeeklyLog.objects
            .filter(user=self.request.user)
            .annotate(
                daily_logs_count=Count('dailylog', distinct=True),
                glucoses_count=Count('dailylog__glucoses', distinct=True),
                pressures_count=Count('dailylog__pressures', distinct=True),
                temperature_count=Count('dailylog__body_temperatures', distinct=True),

                avg_calories=Avg('dailylog__calories_count', distinct=True),
                avg_proteins=Avg('dailylog__proteins_count', distinct=True),
                avg_fats=Avg('dailylog__fats_count', distinct=True),
                avg_carbs=Avg('dailylog__carbs_count', distinct=True),

                avg_glucoses=Avg('dailylog__glucoses', distinct=True),
                avg_pressures=Avg('dailylog__pressures', distinct=True),
                avg_temperature=Avg('dailylog__body_temperatures', distinct=True),

                general_health=Avg('dailylog__mood', distinct=True),
            )
            .order_by('-week_end')
        )


def monthly_log_list(request, monthly_log_id):
    """Список ежемесячных отчетов"""

    monthly_log = get_object_or_404(MonthlyLog, user=request.user, id=monthly_log_id)

    monthly_logs = MonthlyLog.objects.filter(user=request.user).order_by('-created_at')[:10]

    template_name = 'data_tracking/monthly_log_list.html'

    context = {
        'monthly_log': monthly_log,
        'monthly_logs': monthly_logs,
    }

    return render(request, template_name, context)
