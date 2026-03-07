from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.views import APIView

from common_utils.constants import APISchemaTags
from data_tracking.serializers import ReportRequestSerializer, DateFilterRequestSerializer


@extend_schema_view(
    post=extend_schema(
        'Получить отчет',
        tags=[APISchemaTags.REPORTS],
        request=ReportRequestSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: {},
        },
    ),
)
class ReportAPIView(APIView):
    """Сгенерировать отчет со всеми данными за период"""

    @staticmethod
    def post(request, *args, **kwargs):
        """Получить данные отчета"""
