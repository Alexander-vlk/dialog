from django.urls import path

from auth_service.templateviews import UserLoginView, UserLogoutView, UserRegisterView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('register/', UserRegisterView.as_view(), name='register'),
]