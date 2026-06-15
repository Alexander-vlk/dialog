from django.core.cache import cache

from auth_service.models import AppUser
from cabinet.selectors import get_user_streak_data


def execute_calculate_streak_for_users() -> None:
    """Подсчитать ударный режим по всем пользователям и сохранить его в Redis"""
    user_streak_redis_key_format = 'app_user:{username}:streak'
    for user in AppUser.objects.filter(is_active=True):
        has_streak = get_user_streak_data(user)
        current_user_streak_redis_key = user_streak_redis_key_format.format(username=user.username)
        user_streak_data = cache.get(current_user_streak_redis_key)
        if not user_streak_data:
            cache.set(
                current_user_streak_redis_key,
                {
                    'days_count': int(has_streak),
                    'is_active': has_streak,
                },
            )
            continue

        user_streak_data['days_count'] += int(has_streak)
        user_streak_data['is_active'] = has_streak
        cache.set(current_user_streak_redis_key, user_streak_data)
