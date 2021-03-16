from django.db import models
from django.utils import timezone
from users.models import ProfileUser

class ReceberEmail(models.Model):
	email = models.ForeignKey(ProfileUser, on_delete = models.CASCADE)
	assunto = models.TextField(max_length = 100)
	resposta = models.TextField(max_length = 100)
	data_resposta = models.CharField(max_length = 100)
