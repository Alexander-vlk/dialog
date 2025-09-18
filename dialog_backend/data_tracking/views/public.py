from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.views import APIView

from constants import SWAGGER_ERROR_MESSAGES, MOOD_SWAGGER_TAG
from data_tracking.serializers import HealthSerializer


@extend_schema(
    tags=[MOOD_SWAGGER_TAG],
    methods=["GET"],
    description='Справочник - виды самочувствия',
    responses={
        status.HTTP_200_OK: HealthSerializer,
        **SWAGGER_ERROR_MESSAGES,
    },
)
class MoodAPIView(APIView):
    """Получить виды самочувствия, которые можно внести в систему"""

    authentication_classes: list = []
    permission_classes: list = []

    serializer_class = HealthSerializer

    def get(self, request):
        """GET-запрос"""
