from django import forms
from usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': "Escolha um nome único (letras, números e @/./+/-/_).",
            'email': "Usado para recuperação de senha e notificações.",
            'password1': "Sua senha deve ter pelo menos 8 caracteres e não pode ser muito comum.",
            'password2': "Digite a mesma senha para verificação.",
        }


class UsuarioLoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))