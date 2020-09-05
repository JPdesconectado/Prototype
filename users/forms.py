from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ProfileUser

class ProfileUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Senha:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha:', widget=forms.PasswordInput)
    class Meta:
            model = ProfileUser
            fields = ('username', 'nome', 'email', 'data_nascimento', 'cadastro_pf',)

            help_texts = {
            'username': None,
            'nome': None,
            'email': None,
            'password1': None,
            'password2': None,
            'cadastro_pf': None,
            }


class ProfileUserChangeForm(UserChangeForm):

    class Meta:
        model = ProfileUser
        fields = ('username', 'nome', 'email', 'data_nascimento', 'cadastro_pf',)        