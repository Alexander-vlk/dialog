from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg, Sum, Max, Q
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView

from data_tracking.forms import DailyLogForm, WeeklyLogForm, MonthlyLogForm
from data_tracking.models import DailyLog, WeeklyLog, MonthlyLog, Health, Glucose, BodyTemperature, Pressure


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


class DailyLogDetailView(DetailView):
    """Страница детальной информации о дневном отчете"""

    template_name = 'data_tracking/daily_log/daily_log_detail.html'
    context_object_name = 'daily_log'
    model = DailyLog

    def get_context_data(self, **kwargs):
        """Получить контекст"""
        context = super().get_context_data(**kwargs)

        glucose_per_day = Glucose.objects.filter(daily_log=self.object)
        pressure_per_day = Pressure.objects.filter(daily_log=self.object)
        temperature_per_day = BodyTemperature.objects.filter(daily_log=self.object)

        context.update({
            'avg_glucose': glucose_per_day.aggregate(
                avg_glucose=Avg('level', distinct=True),
            ),
            'avg_temperature': temperature_per_day.aggregate(
                avg_temperature=Avg('temperature', distinct=True),
            ),
            'avg_pressure': pressure_per_day.aggregate(
                avg_systolic=Avg('systolic', distinct=True),
                avg_diastolic=Avg('diastolic', distinct=True),
            ),

            'glucose_count': glucose_per_day.count(),
            'pressure_count': temperature_per_day.count(),
            'temperature_count': pressure_per_day.count(),

            'pressure_logs': pressure_per_day,
            'glucose_logs': glucose_per_day,
            'temperature_logs': temperature_per_day,
        })
        return context


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


@login_required
@require_http_methods(['GET', 'POST'])
def monthly_log_list(request, monthly_log_id):
    """Список ежемесячных отчетов"""
    monthly_log = get_object_or_404(MonthlyLog, user=request.user, id=monthly_log_id)

    monthly_logs = MonthlyLog.objects.filter(user=request.user).order_by('-created_at')[:10]

    weekly_logs_by_month = WeeklyLog.objects.filter(user=request.user, monthly_log=monthly_log).order_by('week_start')
    daily_logs_by_month = DailyLog.objects.filter(weekly_log__in=weekly_logs_by_month).order_by('-date')

    weight_in_month_start = None
    weight_in_month_end = None
    last_bmi = None
    if weekly_logs_by_month:
        weight_in_month_start = weekly_logs_by_month.first().weight
        weight_in_month_end = weekly_logs_by_month.last().weight

        last_bmi = weekly_logs_by_month.last().bmi

    avg_ketones = weekly_logs_by_month.aggregate(Avg('ketones'))
    avg_calories = daily_logs_by_month.aggregate(Avg('calories_count'))

    most_common_health = (
        Health.objects
        .annotate(
            num_logs=Count(
                'daily_logs',
                filter=Q(
                    daily_logs__in=daily_logs_by_month,
                ),
            ),
        )
        .order_by('-num_logs')
        .first()
    )

    temperature_deviations_count = daily_logs_by_month.aggregate(
        deviations_count=Count(
            'body_temperatures',
            filter=Q(
                body_temperatures__temperature__lte=36.5,
            ) | Q(
                body_temperatures__temperature__gte=37.4,
            ),
            distinct=True,
        )
    )

    template_name = 'data_tracking/monthly_log_list.html'

    context = {
        'monthly_log': monthly_log,
        'monthly_logs': monthly_logs,
        'weight_in_month_start': weight_in_month_start,
        'weight_in_month_end': weight_in_month_end,
        'last_bmi': last_bmi,
        'avg_ketones': avg_ketones,
        'avg_calories': avg_calories,
        'most_common_health': most_common_health,
        'temperature_deviations_count': temperature_deviations_count,
    }

    return render(request, template_name, context)


@login_required
@require_http_methods(['GET', 'POST'])
def edit_monthly_log(request, monthly_log_id):
    """View редактирования ежемесячного отчета"""
    monthly_log = get_object_or_404(MonthlyLog, user=request.user, id=monthly_log_id)
    if request.method == "GET":
        form = MonthlyLogForm(instance=monthly_log)

        context_data = {
            'form': form,
        }
        template_name = 'data_tracking/edit_monthly_log.html'
        return render(request, template_name, context_data)

    form = MonthlyLogForm(request.POST, instance=monthly_log)
    if not form.is_valid():
        return HttpResponseBadRequest()

    form.save()
    reverse_url = reverse('monthly_log', args=[monthly_log.id])
    return redirect(reverse_url)
