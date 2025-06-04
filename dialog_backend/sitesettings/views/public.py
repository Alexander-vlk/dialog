from django.core.cache import cache
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from constants import SWAGGER_ERROR_MESSAGES
from sitesettings.constants import MAIN_PAGE_DATA_TAG, FEATURES_CACHE_KEY
from sitesettings.models.main_page import (
    CallToActionBlock,
    Feature,
)
from sitesettings.serializers import (
    CallToActionBlockSerializer,
    FeatureSerializer,
)
from sitesettings.utils import get_main_page_settings


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
        serializer = self.serializer_class(instance=self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получить объект блока призыва к действию"""
        return CallToActionBlock.objects.filter(show_on_main_page=True)


@extend_schema(
    tags=[MAIN_PAGE_DATA_TAG],
    methods=['GET'],
    responses={
        status.HTTP_200_OK: FeatureSerializer,
        **SWAGGER_ERROR_MESSAGES,
    }
)
class FeatureAPIView(APIView):
    """APIView для получения данных о функционале приложения"""

    authentication_classes: list = []
    permission_classes: list = []

    serializer_class = FeatureSerializer

    def get(self, request, *args, **kwargs):
        """GET-запрос"""
        serializer = self.serializer_class(instance=self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получение queryset-а"""
        features_queryset = cache.get(FEATURES_CACHE_KEY)
        if not features_queryset:
            features_queryset = Feature.objects.all()[:get_main_page_settings().max_functions_count]
            cache.set(FEATURES_CACHE_KEY, features_queryset, 10000)

        return features_queryset
