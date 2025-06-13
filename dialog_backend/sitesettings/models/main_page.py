from django.core.exceptions import ValidationError
from django.db import models

from common_utils.mixins import AutoDateMixin


class HeroActionBlock(AutoDateMixin):
    """Модель блока слогана"""

    slogan = models.CharField(max_length=200, verbose_name='Слоган', unique=True)
    short_description = models.CharField(max_length=400, verbose_name='Краткое описание', unique=True)
    button_text = models.CharField(max_length=50, verbose_name='Текст кнопки')

    show_on_main_page = models.BooleanField(
        verbose_name='Показывать на главной странице',
        help_text='Показывать на сайте можно не более одного блока',
        default=False,
    )

    class Meta:
        verbose_name = 'Блок слогана'
        verbose_name_plural = 'Блоки слогана'

    def __str__(self):
        """Строковое представление"""
        return f'Блок слогана {self.slogan}'

    def clean(self):
        """Расширение метода валидации"""
        super().clean()
        if not self.show_on_main_page:
            return

        if self.objects.filter(show_on_main_page=True).exclude(pk=self.pk).exists():
            raise ValidationError(
                'Только один блок может быть со включенным статусом "Показывать на главной странице"',
            )


class CallToActionBlock(AutoDateMixin):
    """Модель блока призыва к действию"""

    action_text = models.CharField(max_length=200, verbose_name='Текст призыва', unique=True)
    short_description = models.CharField(max_length=400, verbose_name='Краткое описание', unique=True)
    button_text = models.CharField(max_length=50, verbose_name='Текст кнопки')

    show_on_main_page = models.BooleanField(
        verbose_name='Показывать на главной странице',
        help_text='Показывать на сайте можно не более одного блока',
    )

    class Meta:
        verbose_name = 'Блок призыва к действию'
        verbose_name_plural = 'Блоки призыва к действию'

    def __str__(self):
        """Строковое представление"""
        return f'{self.action_text} (CTA)'

    def clean(self):
        """Расширение метода валидации"""
        super().clean()
        if not self.show_on_main_page:
            return

        if self.objects.filter(show_on_main_page=True).exclude(pk=self.pk).exists():
            raise ValidationError(
                'Только один блок может быть со включенным статусом "Показывать на главной странице"',
            )


class SliderImage(AutoDateMixin):
    """Модель изображения к слайдеру"""

    alt = models.CharField(max_length=100, verbose_name='Альтернативный текст')
    image = models.ImageField(upload_to='slider_images', null=True, blank=True, verbose_name='Изображение')

    show_on_main_page = models.BooleanField(verbose_name='Показывать на главной странице')

    class Meta:
        verbose_name = 'Изображение в слайдере'
        verbose_name_plural = 'Изображения в слайдере'

    def __str__(self):
        """Строковое представление модели"""
        return f'{self.alt}'


class Feature(AutoDateMixin):
    """Модель функций приложения"""

    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.CharField(max_length=400, verbose_name='Описание')
    image = models.ImageField(upload_to='functions', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Функция приложения'
        verbose_name_plural = 'Функции приложения'

class MainPageFAQ(AutoDateMixin):
    """Модель FAQ для главной страницы"""

    question = models.CharField(max_length=400, verbose_name='Вопрос')
    answer = models.CharField(max_length=400, verbose_name='Ответ')

    class Meta:
        verbose_name = 'Вопрос-Ответ для главной страницы'
        verbose_name_plural = 'Вопросы-Ответы для главной страницы'

    def __str__(self):
        """Строковое представление"""
        return f'{self.question} - {self.answer}'
