from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status

from common_utils.constants import APISchemaTags
from data_tracking.viewsets import IndicatorModelViewSet
from data_tracking.models import Temperature
from data_tracking.serializers import TemperatureSerializer, DateFilterRequestSerializer


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект из справочника настроений по его id',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи из справочника настроений',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый тип диабета в справочнике настроений',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_201_CREATED: TemperatureSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект в справочнике настроений',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект в справочнике настроений',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект в справочнике настроений',
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
