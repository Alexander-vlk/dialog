class AvailableIndicators:
    """Доступные виды показателей"""

    TEMPERATURE = 'temperature'
    PRESSURE = 'pressure'
    GLUCOSE = 'glucose'
    HEMOGLOBIN = 'hemoglobin'
    CHOLESTEROL = 'cholesterol'
    LIPID_PROFILE = 'lipid_profile'
    MICROALBUMINURIA = 'microalbuminuria'
    WEIGHT = 'weight'
    KETONES = 'ketones'
    MEAL = 'meal'
    ALL_CHOICES = [
        TEMPERATURE,
        GLUCOSE,
        HEMOGLOBIN,
        CHOLESTEROL,
        LIPID_PROFILE,
        MICROALBUMINURIA,
        WEIGHT,
        KETONES,
        MEAL,
        PRESSURE,
    ]


CARBS_COUNT_BY_SINGLE_BREAD_UNIT = 12
