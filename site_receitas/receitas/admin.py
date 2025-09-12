from django.contrib import admin
from receitas.models import Usuario, Receita

# Register your models here.

#registrando os modelos do usuario e receita
admin.site.register(Usuario)
admin.site.register(Receita)
