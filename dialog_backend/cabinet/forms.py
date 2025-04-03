from django import forms

from cabinet.models import UserProfile
from constants import (
    DIABETES_TYPE_CHOICES,
    GENDER_CHOICES,
    SELECT_INPUT_CLASS,
    TREATMENTS_TYPE_CHOICES,
    TEXT_INPUT_CLASS,
)


class UserProfileEditForm(forms.ModelForm):
    """Форма редактирования профиля пользователя"""

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': TEXT_INPUT_CLASS}),
        label='Имя пользователя',
        required=False,
    )
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': TEXT_INPUT_CLASS}),
        label='Имя',
        required=False,
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': TEXT_INPUT_CLASS}),
        label='Фамилия',
        required=False,
    )
    patronymic_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': TEXT_INPUT_CLASS}),
        label='Отчество',
        required=False,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': TEXT_INPUT_CLASS}),
        label='Email',
        required=False,
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        label='Фото профиля',
        required=False,
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': SELECT_INPUT_CLASS}),
        label='Пол',
    )
    birth_date = forms.DateField(
        required=True,
        label='Дата рождения',
        widget=forms.DateInput(attrs={'class': 'w-full mt-1 p-2 border rounded-l', 'type': 'date'}, format='%Y-%m-%d',),
    )
    diabetes_type = forms.ChoiceField(
        choices=DIABETES_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': SELECT_INPUT_CLASS}),
        label='Тип диабета',
        required=False,
    )
    diagnosis_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': SELECT_INPUT_CLASS}, format='%Y-%m-%d'),
        label='Дата постановки диагноза',
        required=False,
    )
    treatment_type = forms.ChoiceField(
        choices=TREATMENTS_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': SELECT_INPUT_CLASS}),
        label='Тип лечения',
        required=False,
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': TEXT_INPUT_CLASS}),
        label='Номер телефона',
        required=False,
    )

    class Meta:
        model = UserProfile
        fields = [
            'image',
            'username',
            'first_name',
            'last_name',
            'patronymic_name',
            'gender',
            'birth_date',
            'diabetes_type',
            'diagnosis_date',
            'treatment_type',
            'phone_number',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.user:
            self.fields['username'].initial = self.instance.user.username
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        if self.cleaned_data.get('username'):
            self.instance.user.username = self.cleaned_data.get('username')
        if self.cleaned_data.get('email'):
            self.instance.user.email = self.cleaned_data.get('email')

        self.instance.user.save()

        return user
