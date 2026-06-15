from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
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
    get_last=extend_schema(
        'Получить последний прием препарата',
        tags=[APISchemaTags.MEDICATION],
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

    @action(detail=False, methods=['get'], url_path='last', url_name='last')
    def get_last(self, request):
        """Получить последний прием лекарства"""
        last_weight = MedicationTake.objects.filter(user=request.user).order_by('taken_at').last()
        serializer = self.get_serializer(last_weight)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получить набор данных на основе пользователя"""
        date_filter_serializer = DateFilterRequestSerializer(data=self.request.query_params)
        date_filter_serializer.is_valid(raise_exception=True)
        time_filter = Q()
        date_start = date_filter_serializer.validated_data.get('date_start')
        date_end = date_filter_serializer.validated_data.get('date_end')
        if date_start and date_end:
            time_filter = Q(taken_at__date__gte=date_start, taken_at__date__lte=date_end)

        return self.model_name.objects.filter(time_filter, user=self.request.user)
