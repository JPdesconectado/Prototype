from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class ProfileUser(AbstractUser):
    nome = models.CharField(max_length = 50)
    email = models.EmailField(max_length=254)
    data_nascimento = models.DateField(null = True, verbose_name = "Data de Nascimento")
    
    def __str__(self):
        return self.nome
    
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)