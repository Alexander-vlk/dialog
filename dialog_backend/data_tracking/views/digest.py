from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from common_utils.constants import APISchemaTags
from common_utils.mixins import ReadOnlyOrStaffMixin
from data_tracking.models import Mood, Health
from data_tracking.serializers import MoodSerializer, HealthSerializer


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект из справочника настроений по его id',
        tags=[APISchemaTags.MOOD_DIGEST],
        request=MoodSerializer,
        responses={
            status.HTTP_200_OK: MoodSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи из справочника настроений',
        tags=[APISchemaTags.MOOD_DIGEST],
        request=MoodSerializer,
        responses={
            status.HTTP_200_OK: MoodSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый объект в справочнике настроений',
        tags=[APISchemaTags.MOOD_DIGEST],
        request=MoodSerializer,
        responses={
            status.HTTP_200_OK: MoodSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект в справочнике настроений',
        tags=[APISchemaTags.MOOD_DIGEST],
        request=MoodSerializer,
        responses={
            status.HTTP_200_OK: MoodSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект в справочнике настроений',
        tags=[APISchemaTags.MOOD_DIGEST],
        request=MoodSerializer,
        responses={
            status.HTTP_200_OK: MoodSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект в справочнике настроений',
        tags=[APISchemaTags.MOOD_DIGEST],
        request=MoodSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class MoodViewSet(ModelViewSet, ReadOnlyOrStaffMixin):
    """ViewSet для справочника настроений"""

    queryset = Mood.objects.all()
    serializer_class = MoodSerializer


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект из справочника типов состояний по его id',
        tags=[APISchemaTags.HEALTH_DIGEST],
        request=HealthSerializer,
        responses={
            status.HTTP_200_OK: HealthSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи из справочника типов состояний',
        tags=[APISchemaTags.HEALTH_DIGEST],
        request=HealthSerializer,
        responses={
            status.HTTP_200_OK: HealthSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый объект в справочнике типов состояний',
        tags=[APISchemaTags.HEALTH_DIGEST],
        request=HealthSerializer,
        responses={
            status.HTTP_200_OK: HealthSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект в справочнике типов состояний',
        tags=[APISchemaTags.HEALTH_DIGEST],
        request=HealthSerializer,
        responses={
            status.HTTP_200_OK: HealthSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект в справочнике типов состояний',
        tags=[APISchemaTags.HEALTH_DIGEST],
        request=HealthSerializer,
        responses={
            status.HTTP_200_OK: HealthSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект в справочнике типов состояний',
        tags=[APISchemaTags.HEALTH_DIGEST],
        request=HealthSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class HealthViewSet(ModelViewSet, ReadOnlyOrStaffMixin):
    """ViewSet для справочника настроений"""

    queryset = Health.objects.all()
    serializer_class = HealthSerializer
