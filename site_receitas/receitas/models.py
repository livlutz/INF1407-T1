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
    #TODO : tem que mudar o updload para o local correto!!!
    foto_de_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)

    def __str__(self):
        return self.nome

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
    foto_da_receita = models.ImageField(upload_to='fotos_receitas/', null=True, blank=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='receitas')

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