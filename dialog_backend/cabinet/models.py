from django.db import models

from auth_service.models import AppUser
from common_utils.mixins import AutoDateMixin
from common_utils.validators import validate_length


class Disease(AutoDateMixin):
    """Модель сопутствующих болезней"""
    
    users = models.ManyToManyField(
        to=AppUser,
        verbose_name='Пользователи с заболеванием',
        related_name='diseases',
        blank=True,
        help_text='Указанные пользователи болеют этим заболеванием'
    )
    
    name = models.CharField(
        max_length=500,
        verbose_name='Название болезни',
    )
    
    class Meta:
        verbose_name = 'Заболевание'
        verbose_name_plural = 'Заболевания'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Allergy(AutoDateMixin):
    """Класс аллергии"""

    users = models.ManyToManyField(
        to=AppUser,
        verbose_name='Пользователи',
        blank=True,
        related_name='allergies',
        help_text='Указанные пользователи имеют эту аллергию'
    )

    name = models.CharField(
        max_length=500,
        verbose_name='Название аллергии',
    )

    class Meta:
        verbose_name = 'Аллергия'
        verbose_name_plural = 'Аллергии'
        ordering = ['name']


class Advantage(AutoDateMixin):
    """Модель преимуществ"""

    title = models.CharField(max_length=120, verbose_name='Название')
    description = models.CharField(max_length=1000, verbose_name='Описание')

    image = models.ImageField(upload_to='advantages/', blank=True, null=True, verbose_name='Изображение')

    order_num = models.PositiveSmallIntegerField(verbose_name='Порядок', unique=True)

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

        ordering = ['order_num']

    def __str__(self):
        return self.title


class Rate(AutoDateMixin):
    """Модель отзывов"""

    user = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пользователь')

    text = models.CharField(max_length=1000, validators=[validate_length], verbose_name='Текст')

    is_visible = models.BooleanField(verbose_name='Показывать', default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.text[:100]}...'

    @property
    def user_info(self):
        if not self.user:
            return 'Аноним'

        if not self.user.first_name:
            return self.user.username

        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def date_joined(self):
        if not self.user:
            return ''

        return self.user.created_at
