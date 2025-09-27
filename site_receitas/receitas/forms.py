from django import forms
from receitas.models import Receita

"""Cria um formulario baseado no modelo Receita"""
class ReceitaModel2Form(forms.ModelForm):
    class Meta:
        model = Receita
        fields = '__all__'
