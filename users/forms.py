from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset, Field
from .models import ProfileUser

class ProfileUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)
    class Meta:
            model = ProfileUser
            fields = ('username', 'nome', 'email', 'data_nascimento',)
            labels = {
             "nome": "Nome Completo",
            }
            help_texts = {
            'username': None,
            'nome': None,
            'email': None,
            'password1': None,
            'password2': None,
            }
    def __init__(self, *args, **kwargs):
        super(ProfileUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(Column('username', css_class='text-white-75 font-weight-light mb-3')),
            Row(Column('nome', css_class='text-white-75 font-weight-light mb-3')),
            Row(Column('email', css_class='text-white-75 font-weight-light mb-3')),
            Row(Column('password1', css_class='text-white-75 font-weight-light mb-3')),
            Row(Column('password2', css_class='text-white-75 font-weight-light mb-3')),
        )
        self.helper.add_input(Submit('submit', 'Registrar', css_class='btn btn-light btn-xl'))        


class ProfileUserChangeForm(UserChangeForm):

    class Meta:
        model = ProfileUser
        fields = ('username', 'nome', 'email', 'data_nascimento',)        

    def __init__(self, *args, **kwargs):
        super(ProfileUserChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(Column('username', css_class='text-white-75 font-weight-light mb-3')),
            Row(Column('nome', css_class='text-white-75 font-weight-light mb-3')),
            Row(Column('email', css_class='text-white-75 font-weight-light mb-3')),
            Row(Column('password1', css_class='text-white-75 font-weight-light mb-3')),
        )
        self.helper.add_input(Submit('submit', 'Registrar', css_class='btn btn-light btn-xl'))    