from django.db.models import Aggregate, FloatField


class Median(Aggregate):
    """Вычисление медианы"""
    function = 'PERCENTILE_CONT'
    name = 'median'
    output_field = FloatField()
    template = '%(function)s(0.5) WITHIN GROUP (ORDER BY %(expressions)s)'
