from rest_framework.serializers import ModelSerializer
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

from sitesettings.models.main_page import (
    CallToActionBlock,
    Feature,
    HeroActionBlock,
    MainPageFAQ,
    SliderImage,
)


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value={
                'action_text': 'Начните следить за своим здоровьем уже сегодня!',
                'short_description': 'Присоединяйтесь и получите доступ ко всем возможностям бесплатно',
                'button_text': 'Зарегистрироваться',
            },
        ),
    ],
)
class CallToActionBlockSerializer(ModelSerializer):
    """Сериализатор модели CallToActionBlock"""

    class Meta:
        model = CallToActionBlock
        fields = ('action_text', 'short_description', 'button_text')


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value={
                'name': 'Просмотр графиков',
                'description': 'На основе введенных Вами данных строятся графики',
                'image_url': 'https://dialog.com/media/functions/graphics_feature.png',
            },
        ),
    ],
)
class FeatureSerializer(ModelSerializer):
    """Сериализатор модели Feature"""

    class Meta:
        model = Feature
        fields = ('name', 'description', 'image_url')


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value={
                'action_text': 'Контроль диабета — просто и удобно',
                'short_description': 'Следите за своими показателями, анализируйте данные и держите здоровье под контролем',
                'button_text': 'Начать бесплатно',
            },
        ),
    ],
)
class HeroActionBlockSerializer(ModelSerializer):
    """Сериализатор модели HeroActionBlock"""

    class Meta:
        model = HeroActionBlock
        fields = ('slogan', 'short_description', 'button_text')


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'question': 'Вопрос 1',
                    'answer': 'Ответ 1',
                },
                {
                    'question': 'Вопрос 2',
                    'answer': 'Ответ 2',
                },
            ],
        ),
    ],
)
class MainPageFAQSerializer(ModelSerializer):
    """Сериализатор модели MainPageFAQ"""

    class Meta:
        model = MainPageFAQ
        fields = ('question', 'answer')


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'alt': 'Слайд 1',
                    'image_url': 'https://dialog.com/media/slider_images/slide1.png',
                },
                {
                    'alt': 'Слайд 2',
                    'image_url': 'https://dialog.com/media/slider_images/slide2.png',
                },
            ]
        )
    ]
)
class SliderImageSerializer(ModelSerializer):
    """Сериализатор модели SliderImage"""

    class Meta:
        model = SliderImage
        fields = ('alt', 'image_url')
