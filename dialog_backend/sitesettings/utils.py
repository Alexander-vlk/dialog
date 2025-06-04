from django.core.cache import cache

from sitesettings.constants import MAIN_PAGE_SETTINGS_CACHE_KEY
from sitesettings.models.site_settings import MainPageSettings


def get_main_page_settings():
    """Получить настройки главной страницы"""
    main_page_settings = cache.get(MAIN_PAGE_SETTINGS_CACHE_KEY)
    if not main_page_settings:
        main_page_settings = MainPageSettings.objects.last()
        cache.set(MAIN_PAGE_SETTINGS_CACHE_KEY, main_page_settings, 10000)

    return main_page_settings
