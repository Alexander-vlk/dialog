from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy

from auth_service.forms import ExtendedLoginForm, ExtendedUserCreationForm
from constants import TWO_WEEKS


class UserLoginView(LoginView):
    """View для авторизации пользователя"""

    next_page = reverse_lazy('index')
    authentication_form = ExtendedLoginForm

    def form_valid(self, form):
        remember_me = self.request.session.get('remember')
        if remember_me:
            self.request.session.set_expiry(TWO_WEEKS)
        else:
            self.request.session.set_expiry(0)
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    """View для выхода пользователя из аккаунта"""

    next_page = reverse_lazy('index')


class UserRegisterView(CreateView):
    """Регистрация пользователя"""

    template_name = 'registration/register.html'
    form_class = ExtendedUserCreationForm
    next_page = reverse_lazy('index')

    def form_valid(self, form):
        instance = super().form_valid(form)

        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )

        login(self.request, user)

        return instance
