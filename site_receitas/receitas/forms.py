from django import forms
from receitas.models import Receita

class ReceitaModel2Form(forms.ModelForm):
    class Meta:
        model = Receita
        fields = '__all__'
