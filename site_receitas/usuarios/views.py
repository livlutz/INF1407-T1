from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from usuarios.forms import UsuarioModel2Form

# Create your views here.

def login(request):
    return render(request, 'usuarios/login.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def perfil(request):
    return render(request, 'usuarios/perfil.html')

class UsuarioCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': UsuarioModel2Form, }
        return render(request, "usuarios/cadastro.html", contexto)

    def post(self, request, *args, **kwargs):
        formulario = UsuarioModel2Form(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
        usuario.save()
        return HttpResponseRedirect(reverse_lazy("receitas: homepage")) # Não sei se funciona assim
