from django.db import models

from common_utils.mixins import AutoDateMixin


class MainPageSettings(AutoDateMixin):
    """Модель настроек главной страницы"""

    max_slider_images = models.IntegerField(
        verbose_name='Максимальное количество изображений в слайдере'
    )
    max_advantages_count = models.IntegerField(
        verbose_name='Максимальное количество преимуществ'
    )
    max_functions_count = models.IntegerField(
        verbose_name='Максимальное количество функций'
    )
    max_reviews_count = models.IntegerField(
        verbose_name='Максимальное количество отзывов'
    )
    max_faqs_count = models.IntegerField(
        verbose_name='Максимальное количество ответов на вопросы (FAQ)'
    )

    class Meta:
        verbose_name = 'Настройки главной страницы'
        verbose_name_plural = 'Настройки главных страниц'

    def __str__(self):
        return f'Настройки для главной страницы {self.pk}'
