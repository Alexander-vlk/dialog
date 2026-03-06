from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status

from common_utils.constants import APISchemaTags
from data_tracking.viewsets import IndicatorModelViewSet
from data_tracking.models import Temperature
from data_tracking.serializers import TemperatureSerializer, DateFilterRequestSerializer


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект данных температуры пользователя по его id',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи о температуре пользователя',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый объект данных температуры пользователя',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_201_CREATED: TemperatureSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект данных о температуре',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект о температуре',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект данных о температуре',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
)
class TemperatureViewSet(IndicatorModelViewSet):
    """ViewSet для работы с температурой"""

    model_name = Temperature
    serializer_class = TemperatureSerializer
