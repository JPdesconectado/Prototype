from django import forms
from .models import Solicitacao



class FormularioSolicitacao(forms.ModelForm):

	class Meta:
		model = Solicitacao
		fields = ('tipo', 'endereco', 'comentario', 'imagem')