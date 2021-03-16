from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import FileExtensionValidator
from users.models import ProfileUser
from cpf_field.models import CPFField
from django.core.exceptions import ValidationError

TYPE_CHOICE = [
('Defeito No Semáforo', 'Defeito no Semáforo'),
('Estacionamento Irregular', 'Estacionamento Irregular'),
('Sinalização Irregular', 'Sinalização Irregular'),
]

def only_int(value): 
    if value.isdigit()==False:
        raise ValidationError('Utilize somente números.')

class SolicitacaoTransito(models.Model):
    email = models.ForeignKey(ProfileUser, on_delete = models.CASCADE)
    tipo = models.CharField(max_length = 100, choices = TYPE_CHOICE)
    endereco = models.ForeignKey('requests.Endereco', on_delete = models.CASCADE)
    data_criacao = models.DateTimeField(default = timezone.now)
    imagem = models.ImageField(upload_to = 'imagens/')
    comentario = models.TextField(blank=True, default='')

    def __str__(self):
        return self.tipo


class SolicitacaoEducacao(models.Model):
    email = models.ForeignKey(ProfileUser, on_delete = models.CASCADE)
    cadastro_pf = CPFField('CPF')
    rg = models.CharField(max_length = 15, validators=[only_int])
    data_criacao = models.DateTimeField(default = timezone.now)
    escola = models.CharField(max_length = 100)

    def __str__(self):
    	return self.email

class SolicitacaoIluminacao(models.Model):
    email = models.ForeignKey(ProfileUser, on_delete = models.CASCADE)
    conta_luz = models.FileField(upload_to = 'arquivos/')
    rg = models.CharField(max_length = 15, validators=[only_int])
    data_criacao = models.DateTimeField(default = timezone.now)
    comentario = models.CharField(max_length = 100)
    
    def __str__(self):
    	return self.email
    
class SolicitacaoMeioAmbiente(models.Model):
    email = models.ForeignKey(ProfileUser, on_delete = models.CASCADE)
    endereco = models.ForeignKey('requests.Endereco', on_delete = models.CASCADE)
    data_criacao = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.email

class Endereco(models.Model):
    bairro = models.CharField(max_length = 100)
    rua = models.CharField(max_length = 200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length = 200, blank= True)

