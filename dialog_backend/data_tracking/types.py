import datetime

from typing_extensions import TypedDict, NotRequired


class DailyLogData(TypedDict):
    """Типизация для DailyLog"""

    user_id: int
    weekly_log_id: int
    calories_count: int
    proteins_count: int
    fats_count: int
    carbs_count: int
    mood: int
    health_ids: NotRequired[list[int] | None]
    physical_activity: str
    additional_info: str
    date: datetime.date


class DailyLogFillStatus(TypedDict):
    """Типизация для DailyLogFillStatus"""

    date: datetime.date
    is_filled: bool
