from django import forms
from usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.contrib.auth import authenticate

"""Cria um formulário de login para o modelo Usuario"""
class UsuarioLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')

    """Valida o formulário de login e verifica as credenciais do usuário para autenticação."""
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = Usuario.objects.get(email=email)
            except Usuario.DoesNotExist:
                raise forms.ValidationError("Email ou senha inválidos")

            user = authenticate(username=user.username, password=password)
            if not user:
                raise forms.ValidationError("Email ou senha inválidos")
            self.user = user
        return cleaned_data

"""Cria um formulário de criação de usuário personalizado baseado no modelo Usuario"""
class CustomUserCreationForm(UserCreationForm):
    """Define os campos e textos de ajuda para o formulário de criação de usuário."""
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': "Escolha um nome único (letras, números e @/./+/-/_).",
            'email': "Usado para recuperação de senha e notificações.",
            'password1': "Sua senha deve ter pelo menos 8 caracteres e não pode ser muito comum.",
            'password2': "Digite a mesma senha para verificação.",
        }

"""Cria um formulário baseado no modelo Usuario"""
class UsuarioModel2Form(forms.ModelForm):
    """Define os campos, rótulos e widgets para o formulário de usuário."""
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': 'Nome de usuário',
            'email': 'Email',
            'first_name': 'Primeiro nome',
            'last_name': 'Sobrenome',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }