from datetime import timedelta

from drf_spectacular.utils import OpenApiResponse
from rest_framework import status

ONE_DAY = timedelta(days=1)
ONE_WEEK = timedelta(days=7)

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
DIABETES_TYPE_CHOICES = {
    FIRST_TYPE: '1-го типа',
    SECOND_TYPE: '2-го типа',
    MODY_TYPE: 'MODY-диабет',
    GESTATIONAL: 'Гестационный диабет',
    MANY_TYPES: 'Несколько типов диабета',
}

INSULIN_THERAPY = 'insulin_therapy'
PREPARATIONS = 'preparations'
TREATMENTS_TYPE_CHOICES = {
    INSULIN_THERAPY: 'Инсулинотерапия',
    PREPARATIONS: 'Препараты',
}

TEXT_INPUT_CLASS = 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
SELECT_INPUT_CLASS = 'w-full mt-1 p-2 border rounded-lg'
TEXTAREA_INPUT_CLASS = 'w-full resize-y rounded-lg border border-gray-300 p-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent placeholder-gray-400 shadow-sm transition'

DATA_TRACKING_SWAGGER_TAG = 'data-tracking'

SWAGGER_ERROR_MESSAGES = {
    status.HTTP_400_BAD_REQUEST: OpenApiResponse(description='Invalid data'),
    status.HTTP_401_UNAUTHORIZED: OpenApiResponse(description='Not authenticated'),
    status.HTTP_403_FORBIDDEN: OpenApiResponse(description='You have no access to this resource'),
    status.HTTP_404_NOT_FOUND: OpenApiResponse(description='Not found'),
    status.HTTP_405_METHOD_NOT_ALLOWED: OpenApiResponse(description='Method not allowed'),
    status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(description='Internal server error'),
}
