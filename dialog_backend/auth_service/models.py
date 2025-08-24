from django.contrib.auth.models import AbstractUser
from django.db import models

from common_utils.mixins import AutoDateMixin
from common_utils.validators import validate_not_future_date
from constants import TREATMENTS_TYPE_CHOICES, DIABETES_TYPE_CHOICES, GENDER_CHOICES


class AppUser(AbstractUser, AutoDateMixin):
    """Модель пользователя"""

    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True,
        verbose_name="Фото",
        default="images/stub.png",
    )

    patronymic_name = models.CharField(
        max_length=150,
        default="",
        verbose_name="Отчество",
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name="Пол",
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
        validators=[validate_not_future_date],
        null=True,
        blank=True,
    )
    diabetes_type = models.CharField(
        max_length=20,
        choices=DIABETES_TYPE_CHOICES,
        verbose_name="Тип диабета",
        blank=True,
        default="",
    )
    diagnosis_date = models.DateField(
        verbose_name="Дата постановки диагноза",
        validators=[validate_not_future_date],
        null=True,
        blank=True,
    )

    treatment_type = models.ForeignKey(
        "cabinet.TreatmentType",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Тип лечения",
        related_name="users",
    )

    phone_number = models.CharField(
        max_length=15,
        verbose_name="Номер телефона",
        default="",
        blank=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("updated_at",)

    def __str__(self):
        return f"{self.username}"

    @property
    def fio(self):
        return f"{self.last_name} {self.first_name} {self.patronymic_name}"
