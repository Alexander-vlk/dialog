from datetime import timedelta

from django.db.models import Avg
from django.utils import timezone
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from common_utils.constants import APISchemaTags
from data_tracking.serializers.serializers import HealthAppUserSerializer
from data_tracking.viewsets import IndicatorModelViewSet
from data_tracking.models import (
    Temperature,
    Pressure,
    Glucose,
    Hemoglobin,
    Cholesterol,
    LipidProfile,
    Microalbuminuria,
    Weight,
    Ketones,
    Meal,
    PhysicalActivity,
    Note,
    MoodAppUser,
    HealthAppUser,
)
from data_tracking.serializers import (
    TemperatureSerializer,
    PressureSerializer,
    DateFilterRequestSerializer,
    HemoglobinSerializer,
    GlucoseSerializer,
    CholesterolSerializer,
    LipidProfileSerializer,
    MicroalbuminuriaSerializer,
    WeightSerializer,
    KetonesSerializer,
    MealSerializer,
    PhysicalActivitySerializer,
    NoteSerializer,
    MoodAppUserSerializer,
)


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект данных температуры пользователя по его id',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи о температуре пользователя',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
    average=extend_schema(
        'Среднее значение уровня температуры за последние две недели',
        tags=[APISchemaTags.TEMPERATURE],
    ),
    create=extend_schema(
        'Создать новый объект данных температуры пользователя',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_201_CREATED: TemperatureSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект данных о температуре',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект о температуре',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект данных о температуре',
        tags=[APISchemaTags.TEMPERATURE],
        request=TemperatureSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class TemperatureViewSet(IndicatorModelViewSet):
    """ViewSet для работы с температурой"""

    model_name = Temperature
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    @action(detail=False, methods=['get'], url_path='average', url_name='average')
    def average(self, request):
        """Среднее значение температуры"""
        date_end = timezone.now()
        date_start = date_end - timedelta(days=14)
        average = Temperature.objects.filter(
            user=request.user,
            measured_at__gte=date_start,
            measured_at__lte=date_end,
        ).aggregate(Avg('value'))
        return Response(
            {
                'average': average['value__avg'],
            },
            status=status.HTTP_200_OK,
        )


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект данных давления пользователя по его id',
        tags=[APISchemaTags.PRESSURE],
        request=PressureSerializer,
        responses={
            status.HTTP_200_OK: PressureSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи о давлении пользователя',
        tags=[APISchemaTags.PRESSURE],
        request=PressureSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: PressureSerializer,
        },
    ),
    average=extend_schema(
        'Среднее значение давления за последние две недели',
        tags=[APISchemaTags.PRESSURE],
    ),
    create=extend_schema(
        'Создать новый объект данных давления',
        tags=[APISchemaTags.PRESSURE],
        request=PressureSerializer,
        responses={
            status.HTTP_201_CREATED: PressureSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект данных о давлении',
        tags=[APISchemaTags.PRESSURE],
        request=PressureSerializer,
        responses={
            status.HTTP_200_OK: PressureSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект о давлении',
        tags=[APISchemaTags.PRESSURE],
        request=PressureSerializer,
        responses={
            status.HTTP_200_OK: PressureSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект данных о давлении',
        tags=[APISchemaTags.PRESSURE],
        request=PressureSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class PressureViewSet(IndicatorModelViewSet):
    """ViewSet для работы с температурой"""

    model_name = Pressure
    queryset = Pressure.objects.all()
    serializer_class = PressureSerializer

    @action(detail=False, methods=['get'], url_path='average', url_name='average')
    def average(self, request):
        """Среднее значение давления"""
        date_end = timezone.now()
        date_start = date_end - timedelta(days=14)
        average = Pressure.objects.filter(
            user=request.user,
            measured_at__gte=date_start,
            measured_at__lte=date_end,
        ).aggregate(avg_systolic=Avg('systolic'), avg_diastolic=Avg('diastolic'))
        return Response(
            {
                'avg_systolic': average['avg_systolic'],
                'avg_diastolic': average['avg_diastolic'],
            },
            status=status.HTTP_200_OK,
        )


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект данных уровня сахара в крови пользователя по его id',
        tags=[APISchemaTags.GLUCOSE],
        request=GlucoseSerializer,
        responses={
            status.HTTP_200_OK: GlucoseSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи об уровне сахара в крови пользователя',
        tags=[APISchemaTags.GLUCOSE],
        request=GlucoseSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: GlucoseSerializer,
        },
    ),
    average=extend_schema(
        'Среднее значение уровня сахара в крови за последние две недели',
        tags=[APISchemaTags.GLUCOSE],
    ),
    create=extend_schema(
        'Создать новый объект данных уровня сахара в крови пользователя',
        tags=[APISchemaTags.GLUCOSE],
        request=GlucoseSerializer,
        responses={
            status.HTTP_201_CREATED: GlucoseSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект данных об уровне сахара в крови',
        tags=[APISchemaTags.GLUCOSE],
        request=GlucoseSerializer,
        responses={
            status.HTTP_200_OK: GlucoseSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект об уровне сахара в крови',
        tags=[APISchemaTags.GLUCOSE],
        request=GlucoseSerializer,
        responses={
            status.HTTP_200_OK: GlucoseSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект данных уровня сахара в крови',
        tags=[APISchemaTags.GLUCOSE],
        request=GlucoseSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class GlucoseViewSet(IndicatorModelViewSet):
    """ViewSet для работы с уровнем сахара в крови"""

    model_name = Glucose
    queryset = Glucose.objects.all()
    serializer_class = GlucoseSerializer

    @action(detail=False, methods=['get'], url_path='average', url_name='average')
    def average(self, request):
        """Среднее значение уровня сахара в крови"""
        date_end = timezone.now()
        date_start = date_end - timedelta(days=14)
        average = Glucose.objects.filter(
            user=request.user,
            measured_at__gte=date_start,
            measured_at__lte=date_end,
        ).aggregate(Avg('value'))
        return Response(
            {
                'average': average['value__avg'],
            },
            status=status.HTTP_200_OK,
        )


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект данных гемоглобина по его id',
        tags=[APISchemaTags.HEMOGLOBIN],
        request=HemoglobinSerializer,
        responses={
            status.HTTP_200_OK: HemoglobinSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи о гемоглобине пользователя',
        tags=[APISchemaTags.HEMOGLOBIN],
        request=HemoglobinSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: HemoglobinSerializer,
        },
    ),
    average=extend_schema(
        'Среднее значение гемоглобина за последние две недели',
        tags=[APISchemaTags.HEMOGLOBIN],
    ),
    create=extend_schema(
        'Создать новый объект гемоглобина пользователя',
        tags=[APISchemaTags.HEMOGLOBIN],
        request=HemoglobinSerializer,
        responses={
            status.HTTP_201_CREATED: HemoglobinSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект данных гемоглобина',
        tags=[APISchemaTags.HEMOGLOBIN],
        request=HemoglobinSerializer,
        responses={
            status.HTTP_200_OK: HemoglobinSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект гемоглобина',
        tags=[APISchemaTags.HEMOGLOBIN],
        request=HemoglobinSerializer,
        responses={
            status.HTTP_200_OK: HemoglobinSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект данных гемоглобина',
        tags=[APISchemaTags.HEMOGLOBIN],
        request=HemoglobinSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class HemoglobinViewSet(IndicatorModelViewSet):
    """ViewSet для работы с гемоглобином"""

    model_name = Hemoglobin
    queryset = Hemoglobin.objects.all()
    serializer_class = HemoglobinSerializer

    @action(detail=False, methods=['get'], url_path='average', url_name='average')
    def average(self, request):
        """Среднее значение уровня гемоглобина"""
        date_end = timezone.now()
        date_start = date_end - timedelta(days=14)
        average = Hemoglobin.objects.filter(
            user=request.user,
            measured_at__gte=date_start,
            measured_at__lte=date_end,
        ).aggregate(Avg('value'))
        return Response(
            {
                'average': average['value__avg'],
            },
            status=status.HTTP_200_OK,
        )


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект данных холестерина по его id',
        tags=[APISchemaTags.CHOLESTEROL],
        request=CholesterolSerializer,
        responses={
            status.HTTP_200_OK: CholesterolSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи о холестерине пользователя',
        tags=[APISchemaTags.CHOLESTEROL],
        request=CholesterolSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: CholesterolSerializer,
        },
    ),
    average=extend_schema(
        'Среднее значение гемоглобина за последние две недели',
        tags=[APISchemaTags.CHOLESTEROL],
    ),
    create=extend_schema(
        'Создать новый объект холестерина пользователя',
        tags=[APISchemaTags.CHOLESTEROL],
        request=CholesterolSerializer,
        responses={
            status.HTTP_201_CREATED: CholesterolSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект данных холестерина',
        tags=[APISchemaTags.CHOLESTEROL],
        request=CholesterolSerializer,
        responses={
            status.HTTP_200_OK: CholesterolSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект холестерина',
        tags=[APISchemaTags.CHOLESTEROL],
        request=CholesterolSerializer,
        responses={
            status.HTTP_200_OK: CholesterolSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект данных холестерина',
        tags=[APISchemaTags.CHOLESTEROL],
        request=CholesterolSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class CholesterolViewSet(IndicatorModelViewSet):
    """ViewSet для работы с холестерином"""

    model_name = Cholesterol
    queryset = Cholesterol.objects.all()
    serializer_class = CholesterolSerializer

    @action(detail=False, methods=['get'], url_path='average', url_name='average')
    def average(self, request):
        """Среднее значение холестерина"""
        date_end = timezone.now()
        date_start = date_end - timedelta(days=14)
        average = Cholesterol.objects.filter(
            user=request.user,
            measured_at__gte=date_start,
            measured_at__lte=date_end,
        ).aggregate(Avg('value'))
        return Response(
            {
                'average': average['value__avg'],
            },
            status=status.HTTP_200_OK,
        )


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект данных липидного профиля по его id',
        tags=[APISchemaTags.LIPID_PROFILE],
        request=LipidProfileSerializer,
        responses={
            status.HTTP_200_OK: LipidProfileSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи о липидном профиле пользователя',
        tags=[APISchemaTags.LIPID_PROFILE],
        request=LipidProfileSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: LipidProfileSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый объект липидного профиля пользователя',
        tags=[APISchemaTags.LIPID_PROFILE],
        request=LipidProfileSerializer,
        responses={
            status.HTTP_201_CREATED: LipidProfileSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект данных липидного профиля',
        tags=[APISchemaTags.LIPID_PROFILE],
        request=LipidProfileSerializer,
        responses={
            status.HTTP_200_OK: LipidProfileSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект липидного профиля',
        tags=[APISchemaTags.LIPID_PROFILE],
        request=LipidProfileSerializer,
        responses={
            status.HTTP_200_OK: LipidProfileSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект данных липидного профиля',
        tags=[APISchemaTags.LIPID_PROFILE],
        request=LipidProfileSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class LipidProfileViewSet(IndicatorModelViewSet):
    """ViewSet для работы с липидным профилем"""

    model_name = LipidProfile
    queryset = LipidProfile.objects.all()
    serializer_class = LipidProfileSerializer


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект данных микроальбуминурии по его id',
        tags=[APISchemaTags.MICROALBUMINURIA],
        request=MicroalbuminuriaSerializer,
        responses={
            status.HTTP_200_OK: MicroalbuminuriaSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи о микроальбуминурии пользователя',
        tags=[APISchemaTags.MICROALBUMINURIA],
        request=MicroalbuminuriaSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: MicroalbuminuriaSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый объект микроальбуминурии пользователя',
        tags=[APISchemaTags.MICROALBUMINURIA],
        request=MicroalbuminuriaSerializer,
        responses={
            status.HTTP_201_CREATED: MicroalbuminuriaSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект микроальбуминурии',
        tags=[APISchemaTags.MICROALBUMINURIA],
        request=MicroalbuminuriaSerializer,
        responses={
            status.HTTP_200_OK: MicroalbuminuriaSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект микроальбуминурии',
        tags=[APISchemaTags.MICROALBUMINURIA],
        request=MicroalbuminuriaSerializer,
        responses={
            status.HTTP_200_OK: MicroalbuminuriaSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект данных микроальбуминурии',
        tags=[APISchemaTags.MICROALBUMINURIA],
        request=MicroalbuminuriaSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class MicroalbuminuriaViewSet(IndicatorModelViewSet):
    """ViewSet для работы с микроальбуминурией"""

    model_name = Microalbuminuria
    queryset = Microalbuminuria.objects.all()
    serializer_class = MicroalbuminuriaSerializer


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект данных веса по его id',
        tags=[APISchemaTags.WEIGHT],
        request=WeightSerializer,
        responses={
            status.HTTP_200_OK: WeightSerializer,
        },
    ),
    get_last_weight=extend_schema(
        'Получить последний объект данных веса',
        tags=[APISchemaTags.WEIGHT],
        responses={
            status.HTTP_200_OK: WeightSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи о весе пользователя',
        tags=[APISchemaTags.WEIGHT],
        request=WeightSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: WeightSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый объект веса пользователя',
        tags=[APISchemaTags.WEIGHT],
        request=WeightSerializer,
        responses={
            status.HTTP_201_CREATED: WeightSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект веса',
        tags=[APISchemaTags.WEIGHT],
        request=WeightSerializer,
        responses={
            status.HTTP_200_OK: WeightSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект веса',
        tags=[APISchemaTags.WEIGHT],
        request=WeightSerializer,
        responses={
            status.HTTP_200_OK: WeightSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект данных веса',
        tags=[APISchemaTags.WEIGHT],
        request=WeightSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class WeightViewSet(IndicatorModelViewSet):
    """ViewSet для работы с весом"""

    model_name = Weight
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer

    @action(detail=False, methods=['get'], url_path='last', url_name='last')
    def get_last_weight(self, request):
        """Получить последний замер веса"""
        last_weight = Weight.objects.filter(user=request.user).order_by('measured_at').last()
        serializer = self.get_serializer(last_weight)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект данных кетонового профиля по его id',
        tags=[APISchemaTags.KETONES],
        request=KetonesSerializer,
        responses={
            status.HTTP_200_OK: KetonesSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи о кетоновом профиле пользователя',
        tags=[APISchemaTags.KETONES],
        request=KetonesSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: KetonesSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый объект кетонового профиля пользователя',
        tags=[APISchemaTags.KETONES],
        request=KetonesSerializer,
        responses={
            status.HTTP_201_CREATED: KetonesSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект кетонового профиля',
        tags=[APISchemaTags.KETONES],
        request=KetonesSerializer,
        responses={
            status.HTTP_200_OK: KetonesSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект кетонового профиля',
        tags=[APISchemaTags.KETONES],
        request=KetonesSerializer,
        responses={
            status.HTTP_200_OK: KetonesSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект данных кетонового профиля',
        tags=[APISchemaTags.KETONES],
        request=KetonesSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class KetonesViewSet(IndicatorModelViewSet):
    """ViewSet для работы с кетоновыми телами"""

    model_name = Ketones
    queryset = Ketones.objects.all()
    serializer_class = KetonesSerializer


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект данных приема пищи по его id',
        tags=[APISchemaTags.MEAL],
        request=MealSerializer,
        responses={
            status.HTTP_200_OK: MealSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи о приеме пищи пользователя',
        tags=[APISchemaTags.MEAL],
        request=MealSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: MealSerializer,
        },
    ),
    average=extend_schema(
        'Получить средние показатели приемов пищи пользователя',
        tags=[APISchemaTags.MEAL],
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: MealSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый объект приема пищи пользователя',
        tags=[APISchemaTags.MEAL],
        request=MealSerializer,
        responses={
            status.HTTP_201_CREATED: MealSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект приема пищи',
        tags=[APISchemaTags.MEAL],
        request=MealSerializer,
        responses={
            status.HTTP_200_OK: MealSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект приема пищи',
        tags=[APISchemaTags.MEAL],
        request=MealSerializer,
        responses={
            status.HTTP_200_OK: MealSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект данных приема пищи',
        tags=[APISchemaTags.MEAL],
        request=MealSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class MealViewSet(IndicatorModelViewSet):
    """ViewSet для работы с приемами пищи"""

    model_name = Meal
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(detail=False, methods=['get'], url_path='average', url_name='average')
    def average(self, request):
        """Среднее значение холестерина"""
        date_end = timezone.now()
        date_start = date_end - timedelta(days=14)
        average = Meal.objects.filter(
            user=request.user,
            eaten_at__gte=date_start,
            eaten_at__lte=date_end,
        ).aggregate(
            average_calories=Avg('calories'),
            average_proteins=Avg('proteins'),
            average_carbs=Avg('carbs'),
            average_fats=Avg('fats'),
        )
        return Response(
            {
                'average_calories': average['average_calories'],
                'average_proteins': average['average_proteins'],
                'average_carbs': average['average_carbs'],
                'average_fats': average['average_fats'],
            },
            status=status.HTTP_200_OK,
        )


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект данных физической активности по его id',
        tags=[APISchemaTags.PHYSICAL_ACTIVITY],
        request=PhysicalActivitySerializer,
        responses={
            status.HTTP_200_OK: PhysicalActivitySerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи о физической активности пользователя',
        tags=[APISchemaTags.PHYSICAL_ACTIVITY],
        request=PhysicalActivitySerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: PhysicalActivitySerializer,
        },
    ),
    create=extend_schema(
        'Создать новый объект физической активности пользователя',
        tags=[APISchemaTags.PHYSICAL_ACTIVITY],
        request=PhysicalActivitySerializer,
        responses={
            status.HTTP_201_CREATED: PhysicalActivitySerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект физической активности',
        tags=[APISchemaTags.PHYSICAL_ACTIVITY],
        request=PhysicalActivitySerializer,
        responses={
            status.HTTP_200_OK: PhysicalActivitySerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект физической активности',
        tags=[APISchemaTags.PHYSICAL_ACTIVITY],
        request=PhysicalActivitySerializer,
        responses={
            status.HTTP_200_OK: PhysicalActivitySerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект данных физической активности',
        tags=[APISchemaTags.PHYSICAL_ACTIVITY],
        request=PhysicalActivitySerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class PhysicalActivityViewSet(IndicatorModelViewSet):
    """ViewSet для работы с физической активностью"""

    model_name = PhysicalActivity
    queryset = PhysicalActivity.objects.all()
    serializer_class = PhysicalActivitySerializer


@extend_schema_view(
    retrieve=extend_schema(
        'Получить один объект заметки по его id',
        tags=[APISchemaTags.NOTES],
        request=NoteSerializer,
        responses={
            status.HTTP_200_OK: NoteSerializer,
        },
    ),
    list=extend_schema(
        'Получить все записи заметки пользователя',
        tags=[APISchemaTags.NOTES],
        request=NoteSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: NoteSerializer,
        },
    ),
    create=extend_schema(
        'Создать новый объект заметки пользователя',
        tags=[APISchemaTags.NOTES],
        request=NoteSerializer,
        responses={
            status.HTTP_201_CREATED: NoteSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком объект заметки',
        tags=[APISchemaTags.NOTES],
        request=NoteSerializer,
        responses={
            status.HTTP_200_OK: NoteSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить объект заметки',
        tags=[APISchemaTags.NOTES],
        request=NoteSerializer,
        responses={
            status.HTTP_200_OK: NoteSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить объект заметки',
        tags=[APISchemaTags.NOTES],
        request=NoteSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class NoteViewSet(IndicatorModelViewSet):
    """ViewSet для работы с заметками"""

    model_name = Note
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


@extend_schema_view(
    retrieve=extend_schema(
        'Получить связку настроения и пользователя по ее id',
        tags=[APISchemaTags.MOOD],
        request=MoodAppUserSerializer,
        responses={
            status.HTTP_200_OK: MoodAppUserSerializer,
        },
    ),
    list=extend_schema(
        'Получить список связок настроения и пользователя',
        tags=[APISchemaTags.MOOD],
        request=MoodAppUserSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: MoodAppUserSerializer,
        },
    ),
    create=extend_schema(
        'Создать новую связку настроения и пользователя',
        tags=[APISchemaTags.MOOD],
        request=MoodAppUserSerializer,
        responses={
            status.HTTP_201_CREATED: MoodAppUserSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком связку настроения и пользователя',
        tags=[APISchemaTags.MOOD],
        request=MoodAppUserSerializer,
        responses={
            status.HTTP_200_OK: MoodAppUserSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить связку настроения и пользователя',
        tags=[APISchemaTags.MOOD],
        request=MoodAppUserSerializer,
        responses={
            status.HTTP_200_OK: MoodAppUserSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить связку настроения и пользователя',
        tags=[APISchemaTags.MOOD],
        request=MoodAppUserSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class MoodAppUserViewSet(IndicatorModelViewSet):
    """ViewSet для работы со связкой пользователя и настроения"""

    model_name = MoodAppUser
    queryset = MoodAppUser.objects.all()
    serializer_class = MoodAppUserSerializer


@extend_schema_view(
    retrieve=extend_schema(
        'Получить связку состояния и пользователя по ее id',
        tags=[APISchemaTags.HEALTH],
        request=HealthAppUserSerializer,
        responses={
            status.HTTP_200_OK: HealthAppUserSerializer,
        },
    ),
    list=extend_schema(
        'Получить список связок состояния и пользователя',
        tags=[APISchemaTags.HEALTH],
        request=HealthAppUserSerializer,
        parameters=[DateFilterRequestSerializer],
        responses={
            status.HTTP_200_OK: HealthAppUserSerializer,
        },
    ),
    create=extend_schema(
        'Создать новую связку состояния и пользователя',
        tags=[APISchemaTags.HEALTH],
        request=HealthAppUserSerializer,
        responses={
            status.HTTP_201_CREATED: HealthAppUserSerializer,
        },
    ),
    update=extend_schema(
        'Обновить целиком связку состояния и пользователя',
        tags=[APISchemaTags.HEALTH],
        request=HealthAppUserSerializer,
        responses={
            status.HTTP_200_OK: HealthAppUserSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить связку состояния и пользователя',
        tags=[APISchemaTags.HEALTH],
        request=HealthAppUserSerializer,
        responses={
            status.HTTP_200_OK: HealthAppUserSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить связку состояния и пользователя',
        tags=[APISchemaTags.HEALTH],
        request=HealthAppUserSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
)
class HealthAppUserViewSet(IndicatorModelViewSet):
    """ViewSet для работы со связкой пользователя и настроения"""

    model_name = HealthAppUser
    queryset = HealthAppUser.objects.all()
    serializer_class = HealthAppUserSerializer
