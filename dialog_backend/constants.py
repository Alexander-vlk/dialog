from datetime import timedelta

from drf_spectacular.utils import OpenApiResponse
from rest_framework import status

HALF_HOUR = timedelta(minutes=30)
ONE_DAY = timedelta(days=1)
ONE_WEEK = timedelta(days=7)
TWO_MONTHS = timedelta(days=60)

TWO_WEEKS = 1209600

BATCH_SIZE = 1000

MALE = 'MALE'
FEMALE = 'FEMALE'
GENDER_CHOICES = {
    MALE: 'Мужской',
    FEMALE: 'Женский',
}

FIRST_TYPE = '1'
SECOND_TYPE = '2'
MODY_TYPE = 'mody'
GESTATIONAL = 'gestational'
MANY_TYPES = 'many_types'
NO_DIABETES = 'no_diabetes'
DIABETES_TYPE_CHOICES = {
    FIRST_TYPE: '1-го типа',
    SECOND_TYPE: '2-го типа',
    MODY_TYPE: 'MODY-диабет',
    GESTATIONAL: 'Гестационный диабет',
    MANY_TYPES: 'Несколько типов диабета',
    NO_DIABETES: 'Не болею диабетом',
}

TERRIBLE = 1
BAD = 2
NORMAL = 3
GOOD = 4
GREAT = 5
GENERAL_HEALTH_CHOICES = {
    TERRIBLE: 'Ужасное',
    BAD: 'Плохое',
    NORMAL: 'Нормальное',
    GOOD: 'Хорошее',
    GREAT: 'Прекрасное',
}

NOT_SET = 'not_set'
INSULIN_THERAPY = 'insulin_therapy'
PREPARATIONS = 'preparations'
TREATMENTS_TYPE_CHOICES = {
    INSULIN_THERAPY: 'Инсулинотерапия',
    PREPARATIONS: 'Препараты',
    NOT_SET: 'Не указывать',
}

TEXT_INPUT_CLASS = 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
SELECT_INPUT_CLASS = 'w-full mt-1 p-2 border rounded-lg'
TEXTAREA_INPUT_CLASS = 'w-full resize-y rounded-lg border border-gray-300 p-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent placeholder-gray-400 shadow-sm transition'

MONTHLY_LOG_SWAGGER_TAG = 'Ежемесячный отчет'
WEEKLY_LOG_SWAGGER_TAG = 'Еженедельный отчет'
DAILY_LOG_SWAGGER_TAG = 'Дневной отчет'

GLUCOSE_SWAGGER_TAG = 'Глюкоза (уровень сахара в крови)'
PRESSURE_SWAGGER_TAG = 'Давление'
BODY_TEMPERATURE_SWAGGER_TAG = 'Температура тела'
BJU_SWAGGER_TAG = 'БЖУ'
HEALTH_SWAGGER_TAG = 'Состояние здоровья'
MOOD_SWAGGER_TAG = 'Настроение'

SWAGGER_ERROR_MESSAGES = {
    status.HTTP_400_BAD_REQUEST: OpenApiResponse(description='Invalid data'),
    status.HTTP_401_UNAUTHORIZED: OpenApiResponse(description='Not authenticated'),
    status.HTTP_403_FORBIDDEN: OpenApiResponse(
        description='You have no access to this resource'
    ),
    status.HTTP_404_NOT_FOUND: OpenApiResponse(description='Not found'),
    status.HTTP_405_METHOD_NOT_ALLOWED: OpenApiResponse(
        description='Method not allowed'
    ),
    status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
        description='Internal server error'
    ),
}
