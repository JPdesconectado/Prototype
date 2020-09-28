from django import forms
from .models import SolicitacaoTransito, SolicitacaoEducacao, SolicitacaoIluminacao, SolicitacaoUPA, Status

BAIRROS =[
('Água Verde', 'Água Verde'),
('Centro', 'Centro'),

]

class FormularioSolicitacaoTransito(forms.ModelForm):
	bairro = forms.ChoiceField(choices = BAIRROS)
	rua = forms.CharField(max_length = 200)
	numero = forms.IntegerField()
	complemento = forms.CharField(max_length = 200, required = False)

	class Meta:
		model = SolicitacaoTransito
		fields = ('tipo', 'bairro', 'rua', 'numero', 'complemento', 'comentario', 'imagem')


class FormularioSolicitacaoEducacao(forms.ModelForm):
	
	class Meta:
		model = SolicitacaoEducacao
		fields = ('cadastro_pf', 'rg', 'comentario')

class FormularioSolicitacaoIluminacao(forms.ModelForm):
    
    class Meta:
        model = SolicitacaoIluminacao
        fields = ('rg', 'conta_luz', 'comentario')


class FormularioSolicitacaoUPA(forms.ModelForm):

	class Meta:
		model = SolicitacaoUPA
		fields = ('rg', 'card_sus', 'comprovante_residencia')


class FormularioStatus(forms.ModelForm):

	class Meta:
		model = Status
		fields = ('atual',)

