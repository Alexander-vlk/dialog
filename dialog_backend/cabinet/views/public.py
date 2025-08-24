from django.conf import settings
from django.core.cache import cache
from drf_spectacular.utils import extend_schema
from rest_framework import permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from cabinet.models import TreatmentType
from cabinet.serializers import TreatmentTypeResponseSerializer
from constants import HEALTH_SWAGGER_TAG, SWAGGER_ERROR_MESSAGES


class TreatmentTypeAPIView(APIView):
    """ViewSet для TreatmentType"""

    parser_classes = [JSONParser]
    authentication_classes: list = []
    permission_classes: list = [permissions.AllowAny]

    treatment_type_cache_key = 'cabinet:treatment_type'

    @extend_schema(
        operation_id='Получение типов лечения',
        tags=[HEALTH_SWAGGER_TAG],
        description='Получить все данные о доступных типах лечения',
        responses={
            status.HTTP_200_OK: TreatmentTypeResponseSerializer,
            **SWAGGER_ERROR_MESSAGES,
        }
    )
    def get(self, request):
        """Получить все типы лечения"""

        serializer = TreatmentTypeResponseSerializer(self.get_queryset(), many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def get_queryset(self):
        """Получить QuerySet типов лечения"""

        treatment_types = cache.get(self.treatment_type_cache_key)

        if not treatment_types:
            treatment_types = TreatmentType.objects.all()
            cache.set(self.treatment_type_cache_key, treatment_types, timeout=10000 if not settings.DEBUG else 10)

        return treatment_types
