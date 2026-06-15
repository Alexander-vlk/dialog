from dataclasses import dataclass


@dataclass
class StreakData:
    """Данные ударного режима"""

    days_count: int
    is_active: bool
