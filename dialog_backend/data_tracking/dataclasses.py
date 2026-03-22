import datetime
from dataclasses import dataclass
from typing import Any


@dataclass
class DateBounds:
    """Границы временного интервала"""

    date_start: datetime.date
    date_end: datetime.date


@dataclass
class AggregatedIndicatorData:
    """Собранные по показателю данные"""

    total: int
    average_values: dict[str, int]
    median_values: dict[str, int]
    min_value: dict[str, Any] | None
    max_value: dict[str, Any] | None


@dataclass
class DataForReport:
    """Данные для отчета"""

    date_start: datetime.date
    date_end: datetime.date
    aggregated_values: dict[str, AggregatedIndicatorData]
