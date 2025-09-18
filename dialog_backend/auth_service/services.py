from django.conf import settings
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response

from auth_service.constants import REFRESH_TOKEN_COOKIE_NAME
from auth_service.models import AppUser
from auth_service.serializers import AccessTokenResponseSerializer
from constants import TWO_MONTHS, ONE_DAY
from data_tracking.models import DailyLog, MonthlyLog, WeeklyLog


def authenticate_user(request, access_token, refresh_token) -> Response:
    """Аутентифицировать пользователя"""
    response_serializer = AccessTokenResponseSerializer(
        instance={'access': access_token}
    )
    response = Response(response_serializer.data, status.HTTP_201_CREATED)

    response.set_cookie(
        key=REFRESH_TOKEN_COOKIE_NAME,
        value=refresh_token,
        httponly=True,
        secure=not settings.DEBUG,
        samesite='Lax',
        expires=TWO_MONTHS if request.data.get('remember') else ONE_DAY,
    )

    return response


def create_logs_for_new_user(user: AppUser):
    """Создает отчеты для нового пользователя"""
    monthly_log = MonthlyLog.objects.create(
        user=user,
        month=timezone.now().month,
    )

    weekly_log = WeeklyLog.objects.create(
        user=user,
        monthly_log=monthly_log,
        weight=0,
        bmi=0,
        ketones=0,
        week_start=timezone.now(),
        week_end=timezone.now() + timezone.timedelta(days=7),
    )

    DailyLog.objects.create(
        user=user,
        weekly_log=weekly_log,
        calories_count=0,
        proteins_count=0,
        fats_count=0,
        carbs_count=0,
    )
