from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication

from constants import GLUCOSE_SWAGGER_TAG, BODY_TEMPERATURE_SWAGGER_TAG, PRESSURE_SWAGGER_TAG, SWAGGER_ERROR_MESSAGES
from data_tracking.models import BodyTemperature, Glucose, Pressure
from data_tracking.serializers import BodyTemperatureSerializer, GlucoseSerializer, PressureSerializer


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
                enum=['today'],
            )
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
