from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    """Criando a classe usuario
    O usuario terá tudo de AbstractUser mais id e foto de perfil
    """
    id = models.AutoField(primary_key=True)
    email = models.EmailField(help_text='Digite seu email', unique=True)
    foto_de_perfil = models.ImageField(upload_to='usuarios/img', null=True, blank=True)

    class Meta:
        app_label = 'usuarios'

    def __str__(self):
        return self.username
