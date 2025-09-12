from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy

from auth_service.forms import ExtendedLoginForm, ExtendedUserCreationForm
from auth_service.services import create_logs_for_new_user
from constants import TWO_WEEKS


class UserLoginView(LoginView):
    """View для авторизации пользователя"""

    next_page = reverse_lazy("cabinet")
    authentication_form = ExtendedLoginForm

    def form_valid(self, form):
        remember_me = self.request.session.get("remember")
        if remember_me:
            self.request.session.set_expiry(TWO_WEEKS)
        else:
            self.request.session.set_expiry(0)
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    """View для выхода пользователя из аккаунта"""

    next_page = reverse_lazy("index")


class UserRegisterView(CreateView):
    """Регистрация пользователя"""

    template_name = "registration/register.html"
    form_class = ExtendedUserCreationForm
    success_url = reverse_lazy("cabinet")

    def form_valid(self, form):
        instance = super().form_valid(form)

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )

        user.first_name = form.cleaned_data.get("first_name", "")
        user.last_name = form.cleaned_data.get("last_name", "")
        user.email = form.cleaned_data.get("email", "")
        user.save()

        login(self.request, user)

        create_logs_for_new_user(user)

        return instance


class UserPasswordChangeView(PasswordChangeView):
    """View для сброса пароля"""

    template_name = "registration/change_password.html"

    def get_success_url(self):
        cabinet_url = reverse_lazy("cabinet", args=[self.request.user.id])
        return f"{cabinet_url}?success_change_password=true"
