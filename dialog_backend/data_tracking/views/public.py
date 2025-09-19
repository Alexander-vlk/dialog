from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from constants import SWAGGER_ERROR_MESSAGES, HEALTH_SWAGGER_TAG
from data_tracking.models import Mood
from data_tracking.serializers import MoodSerializer


@extend_schema(
    tags=[HEALTH_SWAGGER_TAG],
    methods=['GET'],
    description='Справочник - виды самочувствия',
    responses={
        status.HTTP_200_OK: MoodSerializer,
        **SWAGGER_ERROR_MESSAGES,
    },
)
class MoodAPIView(APIView):
    """Получить виды самочувствия, которые можно внести в систему"""

    authentication_classes: list = []
    permission_classes: list = []

    serializer_class = MoodSerializer

    def get(self, request):
        """GET-запрос"""
        serializer = self.serializer_class(instance=Mood.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
