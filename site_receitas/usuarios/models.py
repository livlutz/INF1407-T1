from django.db import models

# Create your models here.

"""Criando a classe usuario
    O usuario tera id, nome, email, senha e foto de perfil
"""
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='Digite seu nome de usuario')
    email = models.EmailField(help_text='Digite seu email', max_length=254)
    senha = models.CharField(max_length=50, help_text='Digite sua senha')
    foto_de_perfil = models.ImageField(upload_to='site_receitas/usuarios/static/img/usuarios', null=True, blank=True)

    class Meta:
        app_label = 'usuarios'
        
    def __str__(self):
        return self.nome
