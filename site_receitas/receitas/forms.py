from django import forms
from receitas.models import Receita

class ReceitaModel2Form(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['titulo', 'foto_da_receita', 'ingredientes', 'modo_de_preparo', 
                    'tempo_de_preparo', 'porcoes', 'categoria', 'visibilidade']