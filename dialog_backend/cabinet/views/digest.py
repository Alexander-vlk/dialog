"""CRUD-ы для справочников"""

from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from cabinet.models import Disease
from cabinet.serializers import (
    DiseaseSerializer,
)
from common_utils.constants import APISchemaTags
from common_utils.mixins import ReadOnlyOrStaffMixin


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект из справочника сопутствующих заболеваний по его id',
        tags=[APISchemaTags.DISEASE],
        request=DiseaseSerializer,
        responses={
            status.HTTP_200_OK: DiseaseSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи из справочника сопутствующих заболеваний',
        tags=[APISchemaTags.DISEASE],
        request=DiseaseSerializer,
        responses={
            status.HTTP_200_OK: DiseaseSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый объект в справочнике сопутствующих заболеваний',
        tags=[APISchemaTags.DISEASE],
        request=DiseaseSerializer,
        responses={
            status.HTTP_201_CREATED: DiseaseSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект в справочнике сопутствующих заболеваний',
        tags=[APISchemaTags.DISEASE],
        request=DiseaseSerializer,
        responses={
            status.HTTP_200_OK: DiseaseSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект в справочнике сопутствующих заболеваний',
        tags=[APISchemaTags.DISEASE],
        request=DiseaseSerializer,
        responses={
            status.HTTP_200_OK: DiseaseSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект из справочника сопутствующих заболеваний',
        tags=[APISchemaTags.DISEASE],
        request=DiseaseSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class DiseaseViewSet(ModelViewSet, ReadOnlyOrStaffMixin):
    """ViewSet для справочника сопутствующих заболеваний"""

    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
