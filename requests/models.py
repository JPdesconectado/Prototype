from django.db import models
from django.utils import timezone
from django.conf import settings
from users.models import ProfileUser
from cpf_field.models import CPFField

TYPE_CHOICE = [
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

class SolicitacaoTransito(models.Model):
    nome = models.ForeignKey(ProfileUser, on_delete = models.CASCADE)
    status = models.ForeignKey('requests.Status', on_delete = models.CASCADE, default=1)
    tipo = models.CharField(max_length = 100, choices = TYPE_CHOICE)
    endereco = models.ForeignKey('requests.Endereco', on_delete = models.CASCADE)
    data_criacao = models.DateTimeField(default = timezone.now)
    imagem = models.ImageField(upload_to = 'imagens/')
    comentario = models.TextField()

    def __str__(self):
        return self.tipo


class SolicitacaoEducacao(models.Model):
    nome = models.ForeignKey(ProfileUser, on_delete = models.CASCADE)
    cadastro_pf = CPFField('CPF')
    rg = models.CharField(max_length = 15)
    data_criacao = models.DateTimeField(default = timezone.now)
    comentario = models.TextField()

    def __str__(self):
    	return self.nome

class SolicitacaoIluminacao(models.Model):
    nome = models.ForeignKey(ProfileUser, on_delete = models.CASCADE)
    conta_luz = models.CharField(max_length = 100)
    rg = models.CharField(max_length = 15)
    data_criacao = models.DateTimeField(default = timezone.now)
    comentario = models.TextField()
    
    def __str__(self):
    	return self.nome
    
class SolicitacaoUPA(models.Model):
    nome = models.ForeignKey(ProfileUser, on_delete = models.CASCADE)
    rg = models.CharField(max_length = 15)
    card_sus = models.CharField(max_length = 20)
    comprovante_residencia = models.CharField(max_length = 50)
    data_criacao = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nome


class Status(models.Model):
    atual = models.CharField(max_length = 100, choices = STATUS_ATUAL, default='Recebido')

class Endereco(models.Model):
    bairro = models.CharField(max_length = 100)
    rua = models.CharField(max_length = 200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length = 200, blank= True)

