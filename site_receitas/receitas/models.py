from django.db import models
from usuarios.models import Usuario
from site_receitas import settings
# Create your models here.

"""Criando a classe receita
    A receita tera id, titulo, ingredientes, modo de preparo, tempo de preparo, porcoes, categoria, foto da receita e autor
"""
class Receita(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, help_text='Digite o titulo da receita')
    ingredientes = models.TextField(help_text='Liste os ingredientes')
    modo_de_preparo = models.TextField(help_text='Descreva o modo de preparo')
    tempo_de_preparo = models.IntegerField(help_text='Tempo de preparo em minutos')
    porcoes = models.IntegerField(help_text='Numero de porcoes/ Quantas pessoas serve')
    categoria = models.CharField(max_length=100, help_text='Categoria da receita (ex: sobremesa, prato principal, etc.)')

    #ele nao ta salvando a imagem no lugar certo de jeito nenhum
    foto_da_receita = models.ImageField(upload_to='receitas/img', null=True, blank=True)

    visibilidade = models.CharField(max_length=10, choices=[('pub', 'Pub'), ('priv', 'Priv')], default='Pub', help_text='Defina se a receita é pública ou privada (Pub ou Priv)')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        app_label = 'receitas'

    def __str__(self):
        return self.titulo

    """Funcao que formata o tempo de preparo para horas e minutos"""
    def tempo_de_preparo_formatado(self):
        horas = self.tempo_de_preparo // 60
        minutos = self.tempo_de_preparo % 60
        partes = []
        if horas > 0:
            partes.append(f"{horas} hora{'s' if horas > 1 else ''}")
        if minutos > 0 or horas == 0:
            partes.append(f"{minutos} minuto{'s' if minutos != 1 else ''}")
        return " e ".join(partes)