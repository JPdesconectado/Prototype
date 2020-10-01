from django import forms
from .models import SolicitacaoTransito, SolicitacaoEducacao, SolicitacaoIluminacao, SolicitacaoUPA
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset, Field
from crispy_forms.bootstrap import PrependedText

BAIRROS =[
('Água Verde', 'Água Verde'),
('Alto Frigorifico', 'Alto Frigorifico'),
('Alto da Tijuca', 'Alto da Tijuca'),
('Alto das Palmeiras', 'Alto das Palmeiras'),
('Boa Vista', 'Boa Vista'),
("Campo d'Água Verde", "Campo d'Água Verde"),
('Centro', 'Centro'),
('Industrial 1', 'Industrial 1'),
('Industrial 2', 'Industrial 2'),
('Jardim Esperança', 'Jardim Esperança'),
('Marcílio Dias', 'Marcílio Dias'),
('Piedade', 'Piedade'),
('Sossego', 'Sossego'),

]

class FormularioSolicitacaoTransito(forms.ModelForm):
    bairro = forms.ChoiceField(choices = BAIRROS)
    rua = forms.CharField(max_length = 200)
    numero = forms.IntegerField()
    complemento = forms.CharField(max_length = 200, required = False)

    class Meta:
        model = SolicitacaoTransito
        fields = ('tipo', 'bairro', 'rua', 'numero', 'complemento', 'comentario', 'imagem')
        labels = {
        "numero": "Número",
        "comentario": "Descrição",
        "imagem": "Anexar Imagem do Ocorrido"

        }
    def __init__(self, *args, **kwargs):
        super(FormularioSolicitacaoTransito, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(Column('tipo', css_class='text-white-75 font-weight-light mb-5')),
            Row(
                Column('bairro', css_class='text-white-75 font-weight-light mb-5'),
                Column('rua', css_class='text-white-75 font-weight-light mb-5'),
                Column('numero', css_class='text-white-75 font-weight-light mb-5'),
                Column('complemento', css_class='text-white-75 font-weight-light mb-5'),
                                    ),
            Row(Column('comentario', css_class='text-white-75 font-weight-light mb-5')),
            Row(Column('imagem', css_class='text-white-75 font-weight-light mb-5')),
            )
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn btn-light btn-xl'))


class FormularioSolicitacaoEducacao(forms.ModelForm):
    
    class Meta:
        model = SolicitacaoEducacao
        fields = ('cadastro_pf', 'rg', 'comentario')
        labels = {
        "cadastro_pf": "CPF",
        "rg": "RG",
        "comentario": "Descrição",
        }
    def __init__(self, *args, **kwargs):
        super(FormularioSolicitacaoEducacao, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(Column('cadastro_pf', css_class='text-white-75 font-weight-light mb-5'),
                Column('rg', css_class='text-white-75 font-weight-light mb-5'),
            ),
            Row(Column('comentario', css_class='text-white-75 font-weight-light mb-5')),
            )
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn btn-light btn-xl'))


class FormularioSolicitacaoIluminacao(forms.ModelForm):
    
    class Meta:
        model = SolicitacaoIluminacao
        fields = ('rg', 'conta_luz', 'comentario')
        labels = {
        "rg": "RG",
        "conta_luz": "Anexar Conta de Luz",
        "comentario": "Descrição",
        }
    def __init__(self, *args, **kwargs):
        super(FormularioSolicitacaoIluminacao, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(Column('rg', css_class='text-white-75 font-weight-light mb-5')),
            Row(Column('conta_luz', css_class='text-white-75 font-weight-light mb-5')),
            Row(Column('comentario', css_class='text-white-75 font-weight-light mb-5')),
        )
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn btn-light btn-xl'))

class FormularioSolicitacaoUPA(forms.ModelForm):

    class Meta:
        model = SolicitacaoUPA
        fields = ('rg', 'card_sus', 'comprovante_residencia')
        labels = {
        "rg": "RG",
        "card_sus": "Números do Cartão SUS",
        "comprovante_residencia": "Anexar Comprovante de Residência",
        }

    def __init__(self, *args, **kwargs):
        super(FormularioSolicitacaoUPA, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(Column('rg', css_class='text-white-75 font-weight-light mb-5')),
            Row(Column('card_sus', css_class='text-white-75 font-weight-light mb-5')),
            Row(Column('comprovante_residencia', css_class='text-white-75 font-weight-light mb-5')),
        )
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn btn-light btn-xl'))