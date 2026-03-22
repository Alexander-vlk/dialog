from dataclasses import asdict

from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from common_utils.constants import APISchemaTags
from data_tracking.dataclasses import DateBounds
from data_tracking.selectors import get_data_for_report
from data_tracking.serializers import ReportRequestSerializer, DateFilterRequestSerializer, ReportResponseSerializer


@extend_schema_view(
    post=extend_schema(
        'Получить отчет',
        tags=[APISchemaTags.REPORTS],
        request=ReportRequestSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: ReportResponseSerializer,
        },
    ),
)
class ReportAPIView(APIView):
    """Сгенерировать отчет со всеми данными за период"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, *args, **kwargs):
        """Получить данные отчета"""
        request_serializer = ReportRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        query_params_serializer = DateFilterRequestSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        # todo: перегнать все врем в aware
        data_for_report = get_data_for_report(
            user=request.user,
            indicators=request_serializer.validated_data['indicators'],
            date_bounds=DateBounds(
                date_start=query_params_serializer.validated_data['date_start'],
                date_end=query_params_serializer.validated_data['date_end'],
            )
        )
        response_serializer = ReportResponseSerializer(asdict(data_for_report))
        return Response(response_serializer.data, status=status.HTTP_200_OK)
