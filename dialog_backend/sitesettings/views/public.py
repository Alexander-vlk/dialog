from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from constants import SWAGGER_ERROR_MESSAGES
from sitesettings.constants import MAIN_PAGE_DATA_TAG
from sitesettings.models.main_page import (
    CallToActionBlock,
)
from sitesettings.serializers import (
    CallToActionBlockSerializer,
)


@extend_schema(
    tags=[MAIN_PAGE_DATA_TAG],
    methods=['GET'],
    responses={
        status.HTTP_200_OK: CallToActionBlockSerializer,
        **SWAGGER_ERROR_MESSAGES,
    }
)
class CallToActionBlockView(APIView):
    """APIView для получения информации о блоке призыва к действию"""

    authentication_classes: list = []
    permission_classes: list = []

    serializer_class = CallToActionBlockSerializer

    def get(self, request, *args, **kwargs):
        """GET-запрос"""
        serializer = self.serializer_class(data=self.get_queryset(), many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получить объект блока призыва к действию"""
        return CallToActionBlock.objects.filter(show_on_main_page=True)
