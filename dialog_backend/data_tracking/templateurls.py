from django.urls import path

from data_tracking.templateviews import (
    daily_log,
    DailyLogListView,
    DailyLogDetailView,
    edit_monthly_log,
    monthly_log_list,
    weekly_log,
    WeeklyLogListView,
)

urlpatterns = [

    path('daily_log', daily_log, name='daily_log'),
    path('weekly_log', weekly_log, name='weekly_log'),
    path('daily_log_list', DailyLogListView.as_view(), name='daily_log_list'),
    path('daily_log/<int:pk>/detail', DailyLogDetailView.as_view(), name='daily_log_detail'),
    path('weekly_log_list', WeeklyLogListView.as_view(), name='weekly_log_list'),
    path('monthly_logs/<int:monthly_log_id>', monthly_log_list, name='monthly_log'),
    path('monthly_logs/<int:monthly_log_id>/edit', edit_monthly_log, name='monthly_log_edit'),
]
