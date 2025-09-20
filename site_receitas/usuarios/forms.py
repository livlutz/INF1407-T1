from django import forms
from usuarios.models import Usuario

class UsuarioModel2Form(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioLoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))