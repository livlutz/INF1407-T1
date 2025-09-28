from django import forms
from usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.contrib.auth import authenticate

class UsuarioLoginForm(forms.Form):
    """Cria um formulário de login para o modelo Usuario"""

    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')

    def clean(self):
        """Valida o formulário de login e verifica as credenciais do usuário para autenticação."""
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


class CustomUserCreationForm(UserCreationForm):
    """Cria um formulário de criação de usuário personalizado baseado no modelo Usuario"""

    class Meta(UserCreationForm.Meta):
        """Define os campos e textos de ajuda para o formulário de criação de usuário."""
        model = Usuario
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': "Escolha um nome único (letras, números e @/./+/-/_).",
            'email': "Usado para recuperação de senha e notificações.",
            'password1': "Sua senha deve ter pelo menos 8 caracteres e não pode ser muito comum.",
            'password2': "Digite a mesma senha para verificação.",
        }

class UsuarioUpdateForm(forms.ModelForm):
    """Cria um formulário baseado no modelo Usuario"""
    class Meta:
        """Define os campos, rótulos e widgets para o formulário de usuário."""
        model = Usuario
        fields = ("username", "email", "foto_de_perfil")
        help_texts = {
            'username': "Atualize seu nome de usuário (letras, números e @/./+/-/_).",
            'email': "Atualize seu email para recuperação de senha e notificações.",
            'foto_de_perfil': "Atualize sua foto de perfil.",
        }

