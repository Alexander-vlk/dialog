from rest_framework.authentication import SessionAuthentication
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from data_tracking.models import BodyTemperature, Glucose, Pressure
from data_tracking.serializers import BodyTemperatureSerializer, GlucoseSerializer, PressureSerializer


class PressureAPIView(APIView):
    """APIView для получения данных о давлении"""

    authentication_classes = [SessionAuthentication]

    serializer_class = PressureSerializer

    def get(self, request):
        """GET-запрос"""
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """POST-запрос"""
        serializer = self.serializer_class(data=request.data, context={'user': request.user})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def options(self, request, *args, **kwargs):
        """OPTIONS-запрос"""

        response_data = {
            'show_pressure_plot': Pressure.objects.filter(created_at=timezone.now()).count() >= 2,
        }

        return Response(response_data, status=status.HTTP_200_OK)


    def get_queryset(self):
        """Получение queryset-а"""
        request = self.request
        query_params = request.query_params

        queryset = Pressure.objects.filter(user=request.user)

        time_period = query_params.get('time_period')
        if time_period == 'today':
            queryset = queryset.filter(daily_log__date=timezone.now())

        return queryset


class GlucoseAPIView(APIView):
    """APIView для получения данных о глюкозе"""

    authentication_classes = [SessionAuthentication]
    serializer_class = GlucoseSerializer

    def get(self, request):
        """GET-запрос"""
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """POST-запрос"""
        serializer = self.serializer_class(data=request.data, context={'user': request.user})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def options(self, request, *args, **kwargs):
        """OPTIONS-запрос"""

        response_data = {
            'show_pressure_plot': Glucose.objects.filter(created_at=timezone.now()).count() >= 2,
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получение queryset-а"""
        request = self.request
        query_params = request.query_params

        queryset = Glucose.objects.filter(user=request.user)

        time_period = query_params.get('time_period')
        if time_period == 'today':
            queryset = queryset.filter(daily_log__date=timezone.now())

        return queryset


class BodyTemperatureAPIView(APIView):
    """APIView для получения данных о температуре тела"""

    authentication_classes = [SessionAuthentication]
    serializer_class = BodyTemperatureSerializer

    def get(self, request):
        """GET-запрос"""
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """POST-запрос"""
        serializer = self.serializer_class(data=request.data, context={'user': request.user})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def options(self, request, *args, **kwargs):
        """OPTIONS-запрос"""

        response_data = {
            'show_pressure_plot': BodyTemperature.objects.filter(created_at=timezone.now()).count() >= 2,
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """Получение queryset-а"""
        request = self.request
        query_params = request.query_params

        queryset = BodyTemperature.objects.filter(user=request.user)

        time_period = query_params.get('time_period')
        if time_period == 'today':
            queryset = queryset.filter(daily_log__date=timezone.now())

        return queryset