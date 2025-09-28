
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from usuarios.forms import CustomUserCreationForm, UsuarioLoginForm, UsuarioUpdateForm
from usuarios.models import Usuario
from receitas.models import Receita
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def logout_confirm(request):
    """Função de confirmar logout"""
    return render(request, 'usuarios/logout.html')

@login_required
def perfil(request, id):
    """Função de mostrar o perfil do usuario logado"""
    usuario = get_object_or_404(Usuario, pk=id)
    contexto = {
        'usuario': usuario,
        'titulo_janela': 'Perfil',
        'titulo_pagina': 'Perfil do Usuário',
    }
    return render(request, 'usuarios/perfil.html', contexto)

def login(request):
    """Função de realizar login"""
    if request.method == 'POST':
        formulario = UsuarioLoginForm(request.POST)
        if formulario.is_valid():
            auth_login(request, formulario.user)
            return redirect('receitas:homepage')
    else:
        formulario = UsuarioLoginForm()

    contexto = {
        'formulario': formulario,
        'titulo_janela': 'Login',
        'titulo_pagina': 'Entrar',
    }
    return render(request, 'usuarios/login.html', contexto)

def deletar(request):
    return render(request, 'usuarios/deletar.html')

#cria o usuario
class UsuarioCreateView(View):
    """View de criar usuario"""
    def get(self, request, *args, **kwargs):
        """função de criar usuario"""
        contexto = { 'formulario': CustomUserCreationForm,
                     'titulo_janela' : 'Cadastro',
                    'titulo_pagina': 'Cadastrar Usuário',
                    'botao' : 'Cadastrar',}
        return render(request, "usuarios/cadastro.html", contexto)

    def post(self, request, *args, **kwargs):
        """função de postar o formulario de criação de usuario"""
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.save()
            return HttpResponseRedirect(reverse_lazy("receitas:homepage"))
        else:
            contexto = {'formulario': formulario, 'mensagem': 'Erro ao completar o cadastro!'}
            return render(request, "usuarios/cadastro.html", contexto)

class UsuarioReadView(View):
    """View de ler/ mostrar usuario usada para mostrar o perfil do usuario"""
    def get(self, request, *args, **kwargs):
        """mostra o perfil do usuario"""
        usuario = Usuario.objects.get(pk=self.kwargs['id'])
        contexto = {'usuario': usuario,
                    'formulario': CustomUserCreationForm(instance=usuario),
                    'titulo_janela' : 'Perfil',
                    'titulo_pagina': 'Perfil do Usuário',
                    'botao' : 'Ver meu perfil',}
        return render(request, "usuarios/perfil.html", contexto)

class UsuarioUpdateView(View):
    """View de atualizar usuario"""
    def get(self, request, id, *args, **kwargs):
        """mostra o formulario de atualizar usuario"""
        usuario = get_object_or_404(Usuario, pk=self.kwargs['id'])
        formulario = UsuarioUpdateForm(instance=usuario)
        contexto = {
            'formulario': formulario,
            'usuario': usuario,
            'titulo_janela': 'Atualizar Perfil',
            'titulo_pagina': 'Atualizar Dados do Usuário',
            'botao': 'Atualizar Perfil',
        }
        return render(request, 'usuarios/atualiza.html', contexto)

    def post(self, request, id, *args, **kwargs):
        """realiza a atualização do usuario a partir do formulario"""
        usuario = get_object_or_404(Usuario, pk=self.kwargs['id'])
        formulario = UsuarioUpdateForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse_lazy('usuarios:perfil', kwargs={'id': id}))
        else:
            contexto = {
                'formulario': formulario,
                'usuario': usuario,
                'titulo_janela': 'Atualizar Perfil',
                'titulo_pagina': 'Atualizar Dados do Usuário',
                'botao': 'Atualizar Perfil',
            }
            return render(request, 'usuarios/atualiza.html', contexto)

class UsuarioDeleteView(View):
    """View de deletar usuario"""
    def get(self, request, id, *args, **kwargs):
        """mostra a confirmação de deletar usuario"""
        usuario = get_object_or_404(Usuario, pk=self.kwargs['id'])
        contexto = {
            'usuario': usuario,
            'titulo_janela': 'Deletar conta',
            'titulo_pagina': 'Deletar Perfil do Usuário',
            'botao': 'Deletar minha conta',
        }
        return render(request, "usuarios/deletar.html", contexto)

    def post(self, request, id, *args, **kwargs):
        """realiza a deleção do usuario"""
        usuario = get_object_or_404(Usuario, pk=self.kwargs['id'])
        usuario.delete()
        return HttpResponseRedirect(reverse_lazy("usuarios:login"))

class ReceitaListView(View):
    """View de listar as receitas do usuario, que inclui receitas publicas e privadas"""
    def get(self, request, id, *args, **kwargs):
        """mostra as receitas do usuario"""
        usuario = Usuario.objects.get(pk=self.kwargs['id'])
        receitas = Receita.objects.filter(autor=usuario)
        contexto = {
            'usuario': usuario,
            'receitas': receitas,
            'titulo_janela': 'Minhas Receitas',
            'titulo_pagina': 'Receitas do Usuário',
        }
        return render(request, "usuarios/ver_minhas_receitas.html", contexto)