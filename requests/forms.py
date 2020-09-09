from django import forms
from .models import Solicitacao, Status

BAIRROS =[
('Água Verde', 'Água Verde'),
('Centro', 'Centro'),

]

class FormularioSolicitacao(forms.ModelForm):
	bairro = forms.ChoiceField(choices = BAIRROS)
	rua = forms.CharField(max_length = 200)
	numero = forms.IntegerField()
	complemento = forms.CharField(max_length = 200, required = False)

	class Meta:
		model = Solicitacao
		fields = ('tipo', 'bairro', 'rua', 'numero', 'complemento', 'comentario', 'imagem')


class FormularioStatus(forms.ModelForm):

	class Meta:
		model = Status
		fields = ('atual',)