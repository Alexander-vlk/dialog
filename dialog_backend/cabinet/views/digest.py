"""CRUD-ы для справочников"""

from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from cabinet.models import DiabetesType, TreatmentType, Disease
from cabinet.serializers import (
    DiabetesTypeSerializer,
    TreatmentTypeSerializer,
    DiseaseSerializer,
)
from common_utils.constants import APISchemaTags
from common_utils.mixins import ReadOnlyOrStaffMixin


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект из справочника типов диабета по его id',
        tags=[APISchemaTags.DIABETES_TYPE],
        request=DiabetesTypeSerializer,
        responses={
            status.HTTP_200_OK: DiabetesTypeSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи из справочника типов диабета',
        tags=[APISchemaTags.DIABETES_TYPE],
        request=DiabetesTypeSerializer,
        responses={
            status.HTTP_200_OK: DiabetesTypeSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый тип диабета в справочнике типов диабета',
        tags=[APISchemaTags.DIABETES_TYPE],
        request=DiabetesTypeSerializer,
        responses={
            status.HTTP_200_OK: DiabetesTypeSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект в справочнике типов диабета',
        tags=[APISchemaTags.DIABETES_TYPE],
        request=DiabetesTypeSerializer,
        responses={
            status.HTTP_200_OK: DiabetesTypeSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект в справочнике типов диабета',
        tags=[APISchemaTags.DIABETES_TYPE],
        request=DiabetesTypeSerializer,
        responses={
            status.HTTP_200_OK: DiabetesTypeSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект из справочника типов диабета',
        tags=[APISchemaTags.DIABETES_TYPE],
        request=DiabetesTypeSerializer,
        responses={
            status.HTTP_200_OK: DiabetesTypeSerializer,
        },
    ),
)
class DiabetesTypeViewSet(ModelViewSet, ReadOnlyOrStaffMixin):
    """ViewSet для справочника типов диабета"""

    queryset = DiabetesType.objects.all()
    serializer_class = DiabetesTypeSerializer


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект из справочника типов лечения по его id',
        tags=[APISchemaTags.TREATMENT_TYPE],
        request=TreatmentTypeSerializer,
        responses={
            status.HTTP_200_OK: TreatmentTypeSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи из справочника типов лечения',
        tags=[APISchemaTags.TREATMENT_TYPE],
        request=TreatmentTypeSerializer,
        responses={
            status.HTTP_200_OK: TreatmentTypeSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый тип диабета в справочнике типов лечения',
        tags=[APISchemaTags.TREATMENT_TYPE],
        request=TreatmentTypeSerializer,
        responses={
            status.HTTP_200_OK: TreatmentTypeSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект в справочнике типов лечения',
        tags=[APISchemaTags.TREATMENT_TYPE],
        request=TreatmentTypeSerializer,
        responses={
            status.HTTP_200_OK: TreatmentTypeSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект в справочнике типов лечения',
        tags=[APISchemaTags.TREATMENT_TYPE],
        request=TreatmentTypeSerializer,
        responses={
            status.HTTP_200_OK: TreatmentTypeSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект из справочника типов лечения',
        tags=[APISchemaTags.TREATMENT_TYPE],
        request=TreatmentTypeSerializer,
        responses={
            status.HTTP_200_OK: TreatmentTypeSerializer,
        },
    ),
)
class TreatmentTypeViewSet(ModelViewSet, ReadOnlyOrStaffMixin):
    """ViewSet для справочника типов лечения"""

    queryset = TreatmentType.objects.all()
    serializer_class = TreatmentTypeSerializer


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
        'Создать новый тип диабета в справочнике сопутствующих заболеваний',
        tags=[APISchemaTags.DISEASE],
        request=DiseaseSerializer,
        responses={
            status.HTTP_200_OK: DiseaseSerializer,
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
            status.HTTP_200_OK: DiseaseSerializer,
        },
    ),
)
class DiseaseViewSet(ModelViewSet, ReadOnlyOrStaffMixin):
    """ViewSet для справочника сопутствующих заболеваний"""

    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
