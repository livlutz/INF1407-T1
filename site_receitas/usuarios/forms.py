from django import forms
from usuarios.models import Usuario

class UsuarioModel2Form(forms.ModelForm): 
    class Meta:
        model = Usuario
        fields = '__all__'
