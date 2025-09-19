from django.conf import settings
from django.core.cache import cache
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from constants import SWAGGER_ERROR_MESSAGES
from cabinet.constants import ADVANTAGES_CACHE_KEY, RATES_CACHE_KEY
from cabinet.models import Advantage, Rate
from cabinet.serializers import AdvantageResponseSerializer, RateResponseSerializer
from sitesettings.constants import (
    CALL_BACK_ACTION_BLOCK_CACHE_KEY,
    FEATURES_CACHE_KEY,
    HERO_ACTION_BLOCK_CACHE_KEY,
    MAIN_PAGE_DATA_TAG,
    MAIN_PAGE_FAQ_CACHE_KEY,
    SLIDER_IMAGE_CACHE_KEY,
)
from sitesettings.models.main_page import (
    CallToActionBlock,
    Feature,
    HeroActionBlock,
    MainPageFAQ,
    SliderImage,
)
from sitesettings.serializers import (
    CallToActionBlockSerializer,
    FeatureSerializer,
    HeroActionBlockSerializer,
    MainPageFAQSerializer,
    SliderImageSerializer,
)
from sitesettings.utils import get_main_page_settings


@extend_schema(
    tags=[MAIN_PAGE_DATA_TAG],
    methods=['GET'],
    responses={
        status.HTTP_200_OK: AdvantageResponseSerializer,
        **SWAGGER_ERROR_MESSAGES,
    },
)
class AdvantageAPIView(APIView):
    """APIVew для получения данных о преимуществах"""

    authentication_classes: list = []
    permission_classes: list = []

    serializer_class = AdvantageResponseSerializer

    def get(self, request, *args, **kwargs):
        """GET-запрос"""
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получение queryset-а"""
        advantages_queryset = cache.get(ADVANTAGES_CACHE_KEY)
        if not advantages_queryset:
            advantages_queryset = Advantage.objects.all()
            cache.set(
                ADVANTAGES_CACHE_KEY,
                advantages_queryset,
                10000 if not settings.DEBUG else 10,
            )

        return advantages_queryset


@extend_schema(
    tags=[MAIN_PAGE_DATA_TAG],
    methods=['GET'],
    responses={
        status.HTTP_200_OK: CallToActionBlockSerializer,
        **SWAGGER_ERROR_MESSAGES,
    },
)
class CallToActionBlockView(APIView):
    """APIView для получения информации о блоке призыва к действию"""

    authentication_classes: list = []
    permission_classes: list = []

    serializer_class = CallToActionBlockSerializer

    def get(self, request, *args, **kwargs):
        """GET-запрос"""
        serializer = self.serializer_class(instance=self.get_queryset())

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получить объект блока призыва к действию"""
        call_back_action_block = cache.get(CALL_BACK_ACTION_BLOCK_CACHE_KEY)
        if not call_back_action_block:
            call_back_action_block = CallToActionBlock.objects.filter(
                show_on_main_page=True
            ).first()
            cache.set(
                CALL_BACK_ACTION_BLOCK_CACHE_KEY,
                call_back_action_block,
                10000 if not settings.DEBUG else 10,
            )

        return call_back_action_block


@extend_schema(
    tags=[MAIN_PAGE_DATA_TAG],
    methods=['GET'],
    responses={
        status.HTTP_200_OK: FeatureSerializer,
        **SWAGGER_ERROR_MESSAGES,
    },
)
class FeatureAPIView(APIView):
    """APIView для получения данных о функционале приложения"""

    authentication_classes: list = []
    permission_classes: list = []

    serializer_class = FeatureSerializer

    def get(self, request, *args, **kwargs):
        """GET-запрос"""
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получение queryset-а"""
        features_queryset = cache.get(FEATURES_CACHE_KEY)
        if not features_queryset:
            features_queryset = Feature.objects.all()[
                : get_main_page_settings().max_functions_count
            ]
            cache.set(
                FEATURES_CACHE_KEY,
                features_queryset,
                10000 if not settings.DEBUG else 10,
            )

        return features_queryset


@extend_schema(
    tags=[MAIN_PAGE_DATA_TAG],
    methods=['GET'],
    responses={
        status.HTTP_200_OK: HeroActionBlockSerializer,
        **SWAGGER_ERROR_MESSAGES,
    },
)
class HeroActionBlockAPIView(APIView):
    """APIView для получения данных о блоке действия"""

    authentication_classes: list = []
    permission_classes: list = []

    serializer_class = HeroActionBlockSerializer

    def get(self, request, *args, **kwargs):
        """GET-запрос"""
        serializer = self.serializer_class(instance=self.get_queryset())

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получение queryset-а"""
        hero_action_block = cache.get(HERO_ACTION_BLOCK_CACHE_KEY)
        if not hero_action_block:
            hero_action_block = HeroActionBlock.objects.filter(
                show_on_main_page=True
            ).first()
            cache.set(
                HERO_ACTION_BLOCK_CACHE_KEY,
                hero_action_block,
                10000 if not settings.DEBUG else 10,
            )

        return hero_action_block


@extend_schema(
    tags=[MAIN_PAGE_DATA_TAG],
    methods=['GET'],
    responses={
        status.HTTP_200_OK: MainPageFAQSerializer,
        **SWAGGER_ERROR_MESSAGES,
    },
)
class MainPageFAQAPIView(APIView):
    """APIView вопросов-ответов"""

    authentication_classes: list = []
    permission_classes: list = []

    serializer_class = MainPageFAQSerializer

    def get(self, request, *args, **kwargs):
        """GET-запрос"""
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получение queryset-а"""
        faq_queryset = cache.get(MAIN_PAGE_FAQ_CACHE_KEY)
        if not faq_queryset:
            faq_queryset = MainPageFAQ.objects.all()[
                : get_main_page_settings().max_faqs_count
            ]
            cache.set(
                MAIN_PAGE_FAQ_CACHE_KEY,
                faq_queryset,
                10000 if not settings.DEBUG else 10,
            )

        return faq_queryset


@extend_schema(
    tags=[MAIN_PAGE_DATA_TAG],
    methods=['GET'],
    responses={
        status.HTTP_200_OK: RateResponseSerializer,
        **SWAGGER_ERROR_MESSAGES,
    },
)
class RateAPIview(APIView):
    """APIView для получения данных об отзывах для главной страницы"""

    authentication_classes: list = []
    permission_classes: list = []

    serializer_class = RateResponseSerializer

    def get(self, request, *args, **kwargs):
        """GET-запрос"""
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получение queryset-а"""
        rate_queryset = cache.get(RATES_CACHE_KEY)
        if not rate_queryset:
            rate_queryset = Rate.objects.filter(is_visible=True)[
                : get_main_page_settings().max_reviews_count
            ]
            cache.set(
                RATES_CACHE_KEY, rate_queryset, 10000 if not settings.DEBUG else 10
            )

        return rate_queryset


@extend_schema(
    tags=[MAIN_PAGE_DATA_TAG],
    methods=['GET'],
    responses={
        status.HTTP_200_OK: SliderImageSerializer,
        **SWAGGER_ERROR_MESSAGES,
    },
)
class SliderImageAPIView(APIView):
    """APIVew получения изображений для слайдера главной страницы"""

    authentication_classes: list = []
    permission_classes: list = []

    serializer_class = SliderImageSerializer

    def get(self, request, *args, **kwargs):
        """GET-запрос"""
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получение queryset-а"""
        faq_queryset = cache.get(SLIDER_IMAGE_CACHE_KEY)
        if not faq_queryset:
            faq_queryset = SliderImage.objects.filter(
                show_on_main_page=True,
            )[: get_main_page_settings().max_slider_images]
            cache.set(
                SLIDER_IMAGE_CACHE_KEY,
                faq_queryset,
                10000 if not settings.DEBUG else 10,
            )

        return faq_queryset
