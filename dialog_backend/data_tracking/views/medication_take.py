from django.utils import timezone
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from common_utils.constants import APISchemaTags
from common_utils.mixins import ReadOnlyOrStaffMixin
from data_tracking.models import MedicationTake, Medication
from data_tracking.serializers import MedicationTakeSerializer, DateFilterRequestSerializer, MedicationSerializer
from data_tracking.viewsets import IndicatorModelViewSet


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один препарат из справочника по его id',
        tags=[APISchemaTags.MEDICATION],
        request=MedicationSerializer,
        responses={
            status.HTTP_200_OK: MedicationSerializer,
        },
    ),
    list=extend_schema(
        'Получить все препараты из справочника',
        tags=[APISchemaTags.MEDICATION],
        request=MedicationSerializer,
        responses={
            status.HTTP_200_OK: MedicationSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый препарат в справочнике',
        tags=[APISchemaTags.MEDICATION],
        request=MedicationSerializer,
        responses={
            status.HTTP_201_CREATED: MedicationSerializer,
        },
    ),
    update=extend_schema(
        'Полностью обновить препарат в справочнике',
        tags=[APISchemaTags.MEDICATION],
        request=MedicationSerializer,
        responses={
            status.HTTP_200_OK: MedicationSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить препарат в справочнике',
        tags=[APISchemaTags.MEDICATION],
        request=MedicationSerializer,
        responses={
            status.HTTP_200_OK: MedicationSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить препарат из справочника',
        tags=[APISchemaTags.MEDICATION],
        request=MedicationSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class MedicationViewSet(ModelViewSet, ReadOnlyOrStaffMixin):
    """ViewSet для справочника препаратов"""

    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


@extend_schema_view(
    retrieve=extend_schema(
        'Получить запись о приеме препарата по id',
        tags=[APISchemaTags.MEDICATION],
        request=MedicationTakeSerializer,
        responses={
            status.HTTP_200_OK: MedicationTakeSerializer,
        },
    ),
    list=extend_schema(
        'Получить список приемов препаратов',
        tags=[APISchemaTags.MEDICATION],
        request=MedicationTakeSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: MedicationTakeSerializer,
        },
    ),
    create=extend_schema(
        'Создать запись о приеме препарата',
        tags=[APISchemaTags.MEDICATION],
        request=MedicationTakeSerializer,
        responses={
            status.HTTP_201_CREATED: MedicationTakeSerializer,
        },
    ),
    update=extend_schema(
        'Полностью обновить запись о приеме препарата',
        tags=[APISchemaTags.MEDICATION],
        request=MedicationTakeSerializer,
        responses={
            status.HTTP_200_OK: MedicationTakeSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить запись о приеме препарата',
        tags=[APISchemaTags.MEDICATION],
        request=MedicationTakeSerializer,
        responses={
            status.HTTP_200_OK: MedicationTakeSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить запись о приеме препарата',
        tags=[APISchemaTags.MEDICATION],
        request=MedicationTakeSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class MedicationTakeViewSet(IndicatorModelViewSet):
    """ViewSet для работы с приемами препаратов"""

    model_name = MedicationTake
    queryset = MedicationTake.objects.all()
    serializer_class = MedicationTakeSerializer
