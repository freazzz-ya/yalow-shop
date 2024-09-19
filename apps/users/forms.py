from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from PIL import Image

from apps.constants import UserModelConstant
from .models import ClientUser


class CustomUserCreationForm(UserCreationForm):
    """Form for registraton user"""

    username = forms.CharField(
        label='Имя пользователя',
        required=True,
        help_text='Это поле обязательное',
        error_messages={
                'required': 'Это поле обязательное',
        },
    )
    email = forms.EmailField(
        required=True,
        label='email',
        error_messages={
            'required': 'Это поле обязательное',
            'unique': 'Такая почта уже существует',
        },
        help_text='Это поле обязательное',
    )
    description_for_profil = forms.CharField(
        label='Описание профиля',
        help_text='Это поле необязательное',
        required=False,
        empty_value=UserModelConstant.DEFAULT_TEXT_FOR_DESCRIPTION,
    )
    image = forms.ImageField(
        label='Фото профиля',
        help_text='Это поле необязательное',
        required=False,
    )
    telegram_id = forms.IntegerField(
        required=False,
        help_text='Это числовое поле и оно необязательное',
    )
    first_name = forms.CharField(
        label='Имя',
        help_text='Это поле необязательное',
        required=False,
    )
    last_name = forms.CharField(
        label='Фамилия',
        help_text='Это поле необязательное',
        required=False,
    )

    class Meta:
        model = ClientUser
        fields = (
            'username', 'email', 'description_for_profil',
            'image', 'telegram_id', 'first_name', 'last_name',
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Проверяем, загружено ли изображение
        if self.cleaned_data.get('image'):
            img = Image.open(self.cleaned_data['image'])
            img.thumbnail((300, 200))  # Изменяем размер до 300x200
            # Перезаписываем изображение в поле image
            instance.image.save(
                self.cleaned_data['image'].name,
                self.cleaned_data['image'], save=False
            )
        if commit:
            instance.save()
        return instance


class UserAuthenticationForm(AuthenticationForm):
    """Form for Authentication user."""
    
    class Meta:
        model = ClientUser
        fields = (
            'username', 'password'
        )
