from django.db import models
from django.db.models import Q
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from auth_service.permissions import HasRefreshToken
from data_tracking.serializers import DateFilterRequestSerializer


class IndicatorModelViewSet(ModelViewSet):
    """Миксин для создания/обновления показателя"""

    request: Request
    model_name: models.Model

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasRefreshToken]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        """Заполнить user и measured_at"""
        serializer.save(
            user=self.request.user,
            measured_at=timezone.now(),
        )

    def get_queryset(self):
        """Получить набор данных на основе пользователя"""
        # todo: не передаются query-параметры, разобраться
        date_filter_serializer = DateFilterRequestSerializer(data=self.request.query_params)
        date_filter_serializer.is_valid(raise_exception=True)
        time_filter = Q()
        date = date_filter_serializer.validated_data.get('date')
        date_start = date_filter_serializer.validated_data.get('date_start')
        date_end = date_filter_serializer.validated_data.get('date_end')
        if date:
            time_filter = Q(measured_at__date=date)
        elif date_start and date_end:
            time_filter = Q(measured_at__date__gte=date_start, measured_at__date__lte=date_end)

        return self.model_name.objects.filter(time_filter, user=self.request.user)
