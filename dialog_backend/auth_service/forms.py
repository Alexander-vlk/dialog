from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from constants import DIABETES_TYPE_CHOICES, GENDER_CHOICES, TREATMENTS_TYPE_CHOICES

TEXT_INPUT_CLASS = 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'


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
        label='Имя',
        widget=forms.TextInput(attrs={'class': TEXT_INPUT_CLASS}),
    )

    last_name = forms.CharField(
        max_length=150,
        required=True,
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': TEXT_INPUT_CLASS}),
    )

    patronymic_name = forms.CharField(
        required=False,
        max_length=50,
        label='Отчество',
        widget=forms.TextInput(attrs={'class': TEXT_INPUT_CLASS}),
    )

    email = forms.EmailField(
        required=False,
        label='Электронная почта',
        widget=forms.TextInput(attrs={'class': TEXT_INPUT_CLASS}),
    )

    phone_number = forms.CharField(
        required=False,
        label='Номер телефона',
        widget=forms.TextInput(attrs={'class': TEXT_INPUT_CLASS}),
    )

    image = forms.ImageField(
        required=False,
        label='Фото профиля',
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=False,
        label='Пол',
    )

    birth_date = forms.DateField(
        required=True,
        widget=forms.DateInput(format='%d/%m/%Y'),
        label='Дата рождения',
    )

    diagnosis_date = forms.DateField(
        required=False,
        widget=forms.DateInput(format='%d/%m/%Y'),
        label='Дата постановки диагноза',
    )

    diabetes_type = forms.ChoiceField(
        choices=DIABETES_TYPE_CHOICES,
        required=False,
        label='Тип диабета',
    )

    treatment_type = forms.ChoiceField(
        choices=TREATMENTS_TYPE_CHOICES,
        required=False,
        label='Тип лечения',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': TEXT_INPUT_CLASS})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': TEXT_INPUT_CLASS})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': TEXT_INPUT_CLASS})
