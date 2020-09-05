from django.db import models
from django.utils import timezone
from django.conf import settings

TYPE_CHOICE = [
('Acidente', 'Acidente'),
('Defeito No Semáforo', 'Defeito no Semáforo'),
('Estacionamento Irregular', 'Estacionamento Irregular'),
('Sinalização Irregular', 'Sinalização Irregular'),
]


class Solicitacao(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
	tipo = models.CharField(max_length = 100, choices = TYPE_CHOICE)
	endereco = models.CharField(max_length = 200)
	data_criacao = models.DateTimeField(default = timezone.now)
	imagem = models.ImageField(upload_to = 'imagens/')
	comentario = models.TextField()


	def __str__(self):
		return self.tipo