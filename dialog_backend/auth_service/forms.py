from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from constants import (
    DIABETES_TYPE_CHOICES,
    GENDER_CHOICES,
    SELECT_INPUT_CLASS,
    TREATMENTS_TYPE_CHOICES,
    TEXT_INPUT_CLASS,
)


class ExtendedLoginForm(AuthenticationForm):
    """Расширенная форма авторизации"""

    remember = forms.BooleanField(
        required=False,
        initial=False,
    )


class ExtendedUserCreationForm(UserCreationForm):
    """Расширенная форма регистрации"""

    first_name = forms.CharField(
        max_length=150,
        required=True,
        label="Имя",
        widget=forms.TextInput(attrs={"class": TEXT_INPUT_CLASS}),
    )

    last_name = forms.CharField(
        max_length=150,
        required=True,
        label="Фамилия",
        widget=forms.TextInput(attrs={"class": TEXT_INPUT_CLASS}),
    )

    patronymic_name = forms.CharField(
        required=False,
        max_length=50,
        label="Отчество",
        widget=forms.TextInput(attrs={"class": TEXT_INPUT_CLASS}),
    )

    email = forms.EmailField(
        required=False,
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class": TEXT_INPUT_CLASS}),
    )

    phone_number = forms.CharField(
        required=False,
        label="Номер телефона",
        widget=forms.TextInput(attrs={"class": TEXT_INPUT_CLASS}),
    )

    image = forms.ImageField(
        required=False,
        label="Фото профиля",
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=False,
        label="Пол",
        widget=forms.Select(attrs={"class": SELECT_INPUT_CLASS}),
    )

    birth_date = forms.DateField(
        required=True,
        label="Дата рождения",
        widget=forms.DateInput(
            attrs={"class": "w-full mt-1 p-2 border rounded-l", "type": "date"}
        ),
    )

    diagnosis_date = forms.DateField(
        required=False,
        widget=forms.DateInput(format="%d/%m/%Y"),
        label="Дата постановки диагноза",
    )

    diabetes_type = forms.ChoiceField(
        choices=DIABETES_TYPE_CHOICES,
        required=False,
        label="Тип диабета",
        widget=forms.Select(attrs={"class": SELECT_INPUT_CLASS}),
    )

    treatment_type = forms.ChoiceField(
        choices=TREATMENTS_TYPE_CHOICES,
        required=False,
        label="Тип лечения",
        widget=forms.Select(attrs={"class": SELECT_INPUT_CLASS}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = forms.TextInput(
            attrs={"class": TEXT_INPUT_CLASS}
        )
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": TEXT_INPUT_CLASS}
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": TEXT_INPUT_CLASS}
        )
