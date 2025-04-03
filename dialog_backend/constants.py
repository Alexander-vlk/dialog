from datetime import timedelta


ONE_DAY = timedelta(days=1)
ONE_WEEK = timedelta(days=7)

TWO_WEEKS = 1209600

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
