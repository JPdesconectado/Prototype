from django.db import models
from django.utils import timezone
from django.conf import settings

class Solicitacao(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
	tipo = models.CharField(max_length = 200)
	endereco = models.CharField(max_length = 200)
	data_criacao = models.DateTimeField(default = timezone.now)
	imagem = models.ImageField(upload_to = 'imagens/')
	comentario = models.TextField()


	def __str__(self):
		return self.tipo