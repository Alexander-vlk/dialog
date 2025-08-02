from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_GET

from cabinet.models import Rate, Advantage
from data_tracking.models import DailyLog, Glucose, Pressure, BodyTemperature, WeeklyLog
from sitesettings.models import (
    CallToActionBlock,
    Feature,
    MainPageFAQ,
    MainPageSettings,
    HeroActionBlock,
    SliderImage,
)


def index(request):
    """View для главной страницы"""
    slider_images_cache_key = 'v1:main_page:slider_images'
    hero_action_block_cache_key = 'v1:main_page:hero_action_block'
    call_action_block_cache_key = 'v1:main_page:call_action_block'
    features_cache_key = 'v1:main_page:features'
    faqs_cache_key = 'v1:main_page:faqs'
    main_page_settings = MainPageSettings.objects.first()

    slider_images = cache.get(slider_images_cache_key)
    if not slider_images:
        slider_images = SliderImage.objects.filter(show_on_main_page=True)[:main_page_settings.max_slider_images]
        cache.set(slider_images_cache_key, slider_images, 10000)

    hero_action_block = cache.get(hero_action_block_cache_key)
    if not hero_action_block:
        hero_action_block = HeroActionBlock.objects.first()
        cache.set(hero_action_block_cache_key, hero_action_block, 10000)

    call_action_block = cache.get(call_action_block_cache_key)
    if not call_action_block:
        call_action_block = CallToActionBlock.objects.first()
        cache.set(call_action_block_cache_key, call_action_block, 10000)

    features = cache.get(features_cache_key)
    if not features:
        features = Feature.objects.all()[:main_page_settings.max_functions_count]
        cache.set(features_cache_key, features, 6000)

    faqs = cache.get(faqs_cache_key)
    if not faqs:
        faqs = MainPageFAQ.objects.all()[:main_page_settings.max_faqs_count]
        cache.set(faqs_cache_key, faqs, 6000)

    context = {
        'rates': Rate.objects.filter(is_visible=True)[:main_page_settings.max_reviews_count],
        'advantages': Advantage.objects.all()[:main_page_settings.max_advantages_count],
        'slider_images': slider_images,
        'hero_action_block': hero_action_block,
        'call_action_block': call_action_block,
        'features': features,
        'faqs': faqs,
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
        'cabinet': request.user,
        'daily_log': daily_log,
        'weekly_log': weekly_log,
        'glucose_per_day_count': glucose_per_day_count,
        'pressure_per_day_count': pressure_per_day_count,
        'temperature_per_day_count': temperature_per_day_count,
    }

    return render(request, 'cabinet/cabinet.html', context)
