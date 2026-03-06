from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status

from common_utils.constants import APISchemaTags
from data_tracking.viewsets import IndicatorModelViewSet
from data_tracking.models import (
    Temperature,
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
)
from data_tracking.serializers import (
    TemperatureSerializer,
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
            status.HTTP_200_OK: TemperatureSerializer,
        },
    ),
)
class TemperatureViewSet(IndicatorModelViewSet):
    """ViewSet для работы с температурой"""

    model_name = Temperature
    serializer_class = TemperatureSerializer


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
            status.HTTP_200_OK: GlucoseSerializer,
        },
    ),
)
class GlucoseViewSet(IndicatorModelViewSet):
    """ViewSet для работы с уровнем сахара в крови"""

    model_name = Glucose
    serializer_class = GlucoseSerializer


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
            status.HTTP_200_OK: HemoglobinSerializer,
        },
    ),
)
class HemoglobinViewSet(IndicatorModelViewSet):
    """ViewSet для работы с гемоглобином"""

    model_name = Hemoglobin
    serializer_class = HemoglobinSerializer


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
            status.HTTP_200_OK: CholesterolSerializer,
        },
    ),
)
class CholesterolViewSet(IndicatorModelViewSet):
    """ViewSet для работы с холестерином"""

    model_name = Cholesterol
    serializer_class = CholesterolSerializer


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
            status.HTTP_200_OK: LipidProfileSerializer,
        },
    ),
)
class LipidProfileViewSet(IndicatorModelViewSet):
    """ViewSet для работы с липидным профилем"""

    model_name = LipidProfile
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
            status.HTTP_200_OK: MicroalbuminuriaSerializer,
        },
    ),
)
class MicroalbuminuriaViewSet(IndicatorModelViewSet):
    """ViewSet для работы с микроальбуминурией"""

    model_name = Microalbuminuria
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
            status.HTTP_200_OK: WeightSerializer,
        },
    ),
)
class WeightViewSet(IndicatorModelViewSet):
    """ViewSet для работы с весом"""

    model_name = Weight
    serializer_class = WeightSerializer


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
            status.HTTP_200_OK: KetonesSerializer,
        },
    ),
)
class KetonesViewSet(IndicatorModelViewSet):
    """ViewSet для работы с кетоновыми телами"""

    model_name = Ketones
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
            status.HTTP_200_OK: MealSerializer,
        },
    ),
)
class MealViewSet(IndicatorModelViewSet):
    """ViewSet для работы с приемами пищи"""

    model_name = Meal
    serializer_class = MealSerializer


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
            status.HTTP_200_OK: PhysicalActivitySerializer,
        },
    ),
)
class PhysicalActivityViewSet(IndicatorModelViewSet):
    """ViewSet для работы с физической активностью"""

    model_name = PhysicalActivity
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
            status.HTTP_200_OK: NoteSerializer,
        },
    ),
)
class NoteViewSet(IndicatorModelViewSet):
    """ViewSet для работы с заметками"""

    model_name = Note
    serializer_class = NoteSerializer
