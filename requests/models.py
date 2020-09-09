from django.db import models
from django.utils import timezone
from django.conf import settings
from users.models import ProfileUser

TYPE_CHOICE = [
('Acidente', 'Acidente'),
('Defeito No Semáforo', 'Defeito no Semáforo'),
('Estacionamento Irregular', 'Estacionamento Irregular'),
('Sinalização Irregular', 'Sinalização Irregular'),
]

STATUS_ATUAL = [
('Recebido', 'Recebido'),
('Em andamento', 'Em andamento'),
('Recusado', 'Recusado'),
('Concluído', 'Concluído'),
]

class Solicitacao(models.Model):
	usuario = models.ForeignKey(ProfileUser, on_delete= models.CASCADE)
	status = models.ForeignKey('requests.Status', on_delete= models.CASCADE, default=1)
	tipo = models.CharField(max_length = 100, choices = TYPE_CHOICE)
	endereco = models.ForeignKey('requests.Endereco', on_delete= models.CASCADE)
	data_criacao = models.DateTimeField(default = timezone.now)
	imagem = models.ImageField(upload_to = 'imagens/')
	comentario = models.TextField()
	

	def __str__(self):
		return self.tipo



class Status(models.Model):
	atual = models.CharField(max_length = 100, choices = STATUS_ATUAL, default='Recebido')

class Endereco(models.Model):
	bairro = models.CharField(max_length = 100)
	rua = models.CharField(max_length = 200)
	numero = models.IntegerField()
	complemento = models.CharField(max_length = 200, blank= True)

