from lib2to3.fixes.fix_input import context

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication

from constants import (
    BODY_TEMPERATURE_SWAGGER_TAG,
    GLUCOSE_SWAGGER_TAG,
    PRESSURE_SWAGGER_TAG,
    SWAGGER_ERROR_MESSAGES,
    WEEKLY_LOG_SWAGGER_TAG,
)
from data_tracking.models import BodyTemperature, Glucose, Pressure, WeeklyLog, MonthlyLog
from data_tracking.serializers import (
    BodyTemperatureSerializer,
    GlucoseSerializer,
    PressureSerializer,
    WeeklyLogSerializer, AverageGlucoseSerializer, CaloriesSerializer,
)
from data_tracking.templateviews import weekly_log


@extend_schema(
    tags=[WEEKLY_LOG_SWAGGER_TAG],
    methods=['GET'],
    responses={
        status.HTTP_200_OK: WeeklyLogSerializer,
        **SWAGGER_ERROR_MESSAGES,
    }
)
class WeeklyLogAPIView(APIView):
    """APIView для еженедельного отчета"""

    authentication_classes = [SessionAuthentication]
    serializer_class = WeeklyLogSerializer

    @extend_schema(
        operation_id='Получение информации о недельном отчете',
        tags=[WEEKLY_LOG_SWAGGER_TAG],
        description='Получение данных о текущем недельном отчете',
    )
    def get(self, request):
        """GET-запрос"""
        serializer = self.serializer_class(self.get_queryset(), context={'user': request.user})

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получение queryset-а"""
        return WeeklyLog.objects.filter(
            user=self.request.user,
            week_start__lte=timezone.now(),
            week_end__gt=timezone.now(),
        ).first()


@extend_schema(
    tags=[PRESSURE_SWAGGER_TAG],
    methods=['OPTIONS', 'GET', 'POST'],
    responses={
        status.HTTP_200_OK: PressureSerializer,
        **SWAGGER_ERROR_MESSAGES,
    },
    description='Данные о давлении',
)
class PressureAPIView(APIView):
    """APIView для получения данных о давлении"""

    authentication_classes = [SessionAuthentication]

    serializer_class = PressureSerializer

    @extend_schema(
        operation_id='Получение данных о давлении',
        tags=[PRESSURE_SWAGGER_TAG],
        parameters=[
            OpenApiParameter(
                'time_period',
                description='Период, за который должны вернуться данные о давлении',
                enum=['today'],
            )
        ],
        examples=[
            OpenApiExample(
                'Ответ с tima_period=today',
                value=[
                    {
                        'created_at': '10:00',
                        'systolic': 120,
                        'diastolic': 80,
                    },
                    {
                        'created_at': '20:00',
                        'systolic': 130,
                        'diastolic': 85,
                    }
                ]
            ),
            OpenApiExample(
                'Ответ без параметров',
                description='Возвращает вообще все данные о давлении за все время',
                value=[
                    {
                        'created_at': '10:00',
                        'systolic': 120,
                        'diastolic': 80,
                    },
                    {
                        'created_at': '20:00',
                        'systolic': 130,
                        'diastolic': 85,
                    },
                    {
                        'created_at': '20:00',
                        'systolic': 110,
                        'diastolic': 75,
                    },
                ],
            ),
        ],
    )
    def get(self, request):
        """GET-запрос"""
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id='Отправка данных о давлении',
        tags=[PRESSURE_SWAGGER_TAG],
        examples=[
            OpenApiExample(
                'Отправка данных о давлении',
                value={
                    'systolic': 120,
                    'diastolic': 80,
                },
            ),
        ],
    )
    def post(self, request):
        """POST-запрос"""
        serializer = self.serializer_class(data=request.data, context={'user': request.user})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def options(self, request, *args, **kwargs):
        """OPTIONS-запрос"""

        response_data = {
            'show_pressure_plot': Pressure.objects.filter(created_at=timezone.now()).count() >= 2,
        }

        return Response(response_data, status=status.HTTP_200_OK)


    def get_queryset(self):
        """Получение queryset-а"""
        request = self.request
        query_params = request.query_params

        queryset = Pressure.objects.filter(user=request.user)

        time_period = query_params.get('time_period')
        if time_period == 'today':
            queryset = queryset.filter(daily_log__date=timezone.now())
        elif time_period == 'week':
            weekly_log = get_object_or_404(
                WeeklyLog,
                user=request.user,
                id=query_params.get('id'),
            )
            queryset = queryset.filter(daily_log__weekly_log=weekly_log)

        return queryset


@extend_schema(
    tags=[GLUCOSE_SWAGGER_TAG],
    methods=['OPTIONS', 'GET', 'POST'],
    responses={
        status.HTTP_200_OK: GlucoseSerializer,
        **SWAGGER_ERROR_MESSAGES,
    },
    description='Process body temperature data',
)
class GlucoseAPIView(APIView):
    """APIView для получения данных о глюкозе"""

    authentication_classes = [SessionAuthentication]
    serializer_class = GlucoseSerializer

    @extend_schema(
        operation_id='Получение данных о глюкозе (уровне сахара в крови)',
        tags=[GLUCOSE_SWAGGER_TAG],
        parameters=[
            OpenApiParameter(
                'time_period',
                description='Период, за который должны вернуться данные о глюкозе (уровне сахара в крови)',
                enum=['today', 'week', 'month'],
            ),
            OpenApiParameter(
                'id',
                description='Идентификатор объекта, который нужно получить',
            ),
        ],
        examples=[
            OpenApiExample(
                'Ответ с tima_period=today',
                value=[
                    {
                        'created_at': '10:00',
                        'level': 3.6,
                    },
                    {
                        'created_at': '20:00',
                        'level': 3.6,
                    },
                ],
            ),
            OpenApiExample(
                'Ответ без параметров',
                description='Возвращает вообще все данные о давлении за все время',
                value=[
                    {
                        'created_at': '10:00',
                        'level': 3.6,
                    },
                    {
                        'created_at': '20:00',
                        'level': 3.6,
                    },
                    {
                        'created_at': '20:00',
                        'level': 3.6,
                    },
                ],
            ),
        ],
    )
    def get(self, request):
        """GET-запрос"""
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id='Обработка данных о глюкозе (уровне сахара в крови)',
        tags=[GLUCOSE_SWAGGER_TAG],
        examples=[
            OpenApiExample(
                'Пример входных данных',
                value={
                    'level': 3.6,
                },
            ),
        ],
    )
    def post(self, request):
        """POST-запрос"""
        serializer = self.serializer_class(data=request.data, context={'user': request.user})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def options(self, request, *args, **kwargs):
        """OPTIONS-запрос"""

        response_data = {
            'show_pressure_plot': Glucose.objects.filter(created_at=timezone.now()).count() >= 2,
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получение queryset-а"""
        request = self.request
        query_params = request.query_params

        queryset = Glucose.objects.filter(user=request.user)

        time_period = query_params.get('time_period')
        if time_period == 'today':
            queryset = queryset.filter(daily_log__date=timezone.now())
        elif time_period == 'week':
            weekly_log = get_object_or_404(
                WeeklyLog,
                user=request.user,
                id=query_params.get('id'),
            )
            queryset = queryset.filter(daily_log__weekly_log=weekly_log)
        elif time_period == 'month':
            monthly_log = get_object_or_404(
                MonthlyLog,
                user=request.user,
                id=query_params.get('id'),
            )
            weekly_logs = WeeklyLog.objects.filter(monthly_log=monthly_log)
            queryset = queryset.filter(daily_log__weekly_log__in=weekly_logs)

        return queryset


@extend_schema(
    tags=[BODY_TEMPERATURE_SWAGGER_TAG],
    methods=['OPTIONS', 'GET', 'POST'],
    responses={
        status.HTTP_200_OK: BodyTemperatureSerializer,
        **SWAGGER_ERROR_MESSAGES,
    },
    description='Process body temperature data',
)
class BodyTemperatureAPIView(APIView):
    """APIView для получения данных о температуре тела"""

    authentication_classes = [SessionAuthentication]
    serializer_class = BodyTemperatureSerializer

    @extend_schema(
        operation_id='get_body_temperature_data',
        tags=[BODY_TEMPERATURE_SWAGGER_TAG],
        description='Returns list of data about body temperature',
        parameters=[
            OpenApiParameter('time_period'),
        ],
    )
    def get(self, request):
        """GET-запрос"""
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id='create_body_temperature_data',
        tags=[BODY_TEMPERATURE_SWAGGER_TAG],
        description='Create new body temperature data',
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(description='Successfully created'),
            **SWAGGER_ERROR_MESSAGES,
        },
    )
    def post(self, request):
        """POST-запрос"""
        serializer = self.serializer_class(data=request.data, context={'user': request.user})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def options(self, request, *args, **kwargs):
        """OPTIONS-запрос"""

        response_data = {
            'show_pressure_plot': BodyTemperature.objects.filter(created_at=timezone.now()).count() >= 2,
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получение queryset-а"""
        request = self.request
        query_params = request.query_params

        queryset = BodyTemperature.objects.filter(user=request.user)

        time_period = query_params.get('time_period')
        if time_period == 'today':
            queryset = queryset.filter(daily_log__date=timezone.now())

        return queryset


@extend_schema(
    tags=[WEEKLY_LOG_SWAGGER_TAG],
    methods=['GET'],
    description='Получение данных о калориях за неделю',
    responses={
        status.HTTP_200_OK: AverageGlucoseSerializer,
        **SWAGGER_ERROR_MESSAGES,
    }
)
class CaloriesAPIView(APIView):
    """APIView для получения данных о калориях"""

    authentication_classes = [SessionAuthentication]
    serializer_class = CaloriesSerializer

    @extend_schema(
        operation_id='Получение списка данных о калориях за неделю',
        tags=[WEEKLY_LOG_SWAGGER_TAG],
    )
    def get(self, request):
        """GET-запрос"""
        current_weekly_log = get_object_or_404(
            WeeklyLog,
            user=request.user,
            week_start__lte=timezone.now(),
            week_end__gt=timezone.now(),
        )

        serializer = self.serializer_class(current_weekly_log, context={'user': request.user})

        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    tags=[GLUCOSE_SWAGGER_TAG],
    methods=['GET'],
    description='Получение среднего значения глюкозы за указанный период',
    responses={
        status.HTTP_200_OK: AverageGlucoseSerializer,
        **SWAGGER_ERROR_MESSAGES,
    }
)
class AverageGlucoseDataAPIView(APIView):
    """APIView получения данных о средней глюкозе за указанный период"""

    authentication_classes = [SessionAuthentication]
    serializer_class = AverageGlucoseSerializer

    @extend_schema(
        operation_id='Получение списка данных о среднем уровне глюкозы за день за указанный период',
        tags=[GLUCOSE_SWAGGER_TAG],
    )
    def get(self, request):
        """GET-запрос"""
        current_weekly_log = get_object_or_404(
            WeeklyLog,
            user=request.user,
            week_start__lte=timezone.now(),
            week_end__gt=timezone.now(),
        )
        serializer = self.serializer_class(current_weekly_log, context={'user': request.user})
        return Response(serializer.data, status=status.HTTP_200_OK)
