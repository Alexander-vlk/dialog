from rest_framework import permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from cabinet.serializers import TreatmentTypeResponseSerializer


class TreatmentTypeViewSet(APIView):
    """ViewSet для TreatmentType"""

    parser_classes = [JSONParser]
    authentication_classes: list = []
    permission_classes: list = [permissions.AllowAny]

    def get(self, request):
        """Получить все типы лечения"""

        serializer = TreatmentTypeResponseSerializer(self.get_queryset(), many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def get_queryset(self):
        """Получить QuerySet типов лечения"""
