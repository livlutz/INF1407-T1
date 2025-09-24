from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from usuarios.forms import CustomUserCreationForm, UsuarioLoginForm
from usuarios.models import Usuario
from receitas.models import Receita
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
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

@login_required
def logout_confirm(request):
    return render(request, 'usuarios/logout.html')

@login_required
def perfil(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    contexto = {
        'usuario': usuario,
        'titulo_janela': 'Perfil',
        'titulo_pagina': 'Perfil do Usuário',
    }
    return render(request, 'usuarios/perfil.html', contexto)

#cria o usuario
class UsuarioCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': CustomUserCreationForm,
                     'titulo_janela' : 'Cadastro',
                    'titulo_pagina': 'Cadastrar Usuário',
                    'botao' : 'Cadastrar',}

        return render(request, "usuarios/cadastro.html", contexto)

    def post(self, request, *args, **kwargs):
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.save()
            return HttpResponseRedirect(reverse_lazy("receitas:homepage"))
        else:
            contexto = {'formulario': formulario, 'mensagem': 'Erro ao completar o cadastro!'}
            return render(request, "usuarios/cadastro.html", contexto)

#lista o perfil do usuario
class UsuarioReadView(View):
    def get(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(pk=id)
        contexto = {'usuario': usuario,
                    'formulario': CustomUserCreationForm(instance=usuario),
                    'titulo_janela' : 'Perfil',
                    'titulo_pagina': 'Perfil do Usuário',
                    'botao' : 'Ver meu perfil',}
        return render(request, "usuarios/perfil.html", contexto)

#atualiza o usuario
class UsuarioUpdateView(View):
    def get(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(pk=id)
        formulario = CustomUserCreationForm(instance=usuario)
        contexto = {'formulario': formulario,
                    'titulo_janela' : 'Atualizar conta',
                    'titulo_pagina': 'Atualizar Perfil do Usuário',
                    'botao' : 'Atualizar meu perfil',}
        return render(request, "usuarios/perfil.html", contexto)

    def post(self, request, *args, **kwargs):
        usuario = get_object_or_404(Usuario, pk=id)
        formulario = CustomUserCreationForm(request.POST, instance=usuario)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.save()
            return HttpResponseRedirect(reverse_lazy("usuarios: perfil"))
        else:
            contexto = {'formulario': formulario, 'mensagem': 'Erro ao atualizar o perfil!'}
            return render(request, "usuarios/perfil.html", contexto)

#deleta o usuario
class UsuarioDeleteView(View):
    def get(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(pk=id)
        contexto = {'usuario': usuario,
                    'titulo_janela' : 'Deletar conta',
                    'titulo_pagina': 'Deletar Perfil do Usuário',
                    'botao' : 'Deletar minha conta',}
        return render(request, "usuarios/deletar.html", contexto)

    def post(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(pk=id)
        usuario.delete()
        return HttpResponseRedirect(reverse_lazy("usuarios: login"))

#lista as receitas do usuario
class ReceitaListView(View):
    def get(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(pk=id)
        receitas = Receita.objects.filter(autor=usuario)
        contexto = {'usuario': usuario,
                    'receitas': receitas,
                    'titulo_janela' : 'Minhas Receitas',
                    'titulo_pagina': 'Receitas do Usuário',}
        return render(request, "usuarios/perfil.html", contexto)


#usuario1 - s12345678@ - u@gmail.com