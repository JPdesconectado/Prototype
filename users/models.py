from django.db import models
from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField

class ProfileUser(AbstractUser):
    
    nome = models.CharField(max_length = 50)
    email = models.EmailField(max_length=254)
    data_nascimento = models.DateField(null = True, verbose_name = "Data de Nascimento")
    cadastro_pf = CPFField('CPF')
    
    def __str__(self):
        return self.nome