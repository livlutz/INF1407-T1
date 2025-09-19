from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from receitas.models import Receita
from django.views.generic.base import View
from usuarios.models import Usuario
from receitas.forms import ReceitaModel2Form
from django.urls.base import reverse_lazy
from django.http.response import HttpResponseRedirect

# Create your views here.

#filtro ta com problema

class ReceitasCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = {'formulario': ReceitaModel2Form,
                    'titulo_pagina': 'Criar Receita',
                    'titulo_janela': 'Criar Nova Receita',
                    'botao': 'Criar Receita', }
        return render(request, 'receitas/criar-receita.html', contexto)

    def post(self, request, *args, **kwargs):
        formulario = ReceitaModel2Form(request.POST)
        if formulario.is_valid():
            receita = formulario.save()
            receita.autor = request.user
            receita.save()
            return HttpResponseRedirect(reverse_lazy("receitas:homepage"))
        else:
            contexto = {'formulario': formulario,'mensagem': 'Erro ao criar receita!'}
            return render(request, 'receitas/criar-receita.html', contexto)


class PubReceitasListView(View):
    def get(self, request, *args, **kwargs):
        pub_receitas = Receita.objects.all()#.filter(visibilidade='Pub').order_by('id')
        contexto = { 'pub_receitas': pub_receitas,
                    'titulo_pagina': 'Home',
                    'titulo_janela': 'Receitas Publicas',
            }
        return render(
            request,
            'receitas/home.html',
            contexto)

class ReceitasUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        receita = Receita.objects.get(id=id)
        formulario = ReceitaModel2Form(instance=receita)
        contexto = {'formulario': formulario,
                    'titulo_pagina': 'Editar',
                    'titulo_janela': 'Editar Receita',
                    'botao': 'Salvar', }
        return render(request, 'receitas/editar-receita.html', contexto)

    def post(self, request, id, *args, **kwargs):
        receita = get_object_or_404(Receita, id=id)
        formulario = ReceitaModel2Form(request.POST, instance=receita)
        if formulario.is_valid():
            receita = formulario.save()
            receita.autor = request.user
            receita.save()
            return HttpResponseRedirect(reverse_lazy("receitas:homepage"))
        else:
            contexto = {'formulario': formulario,'mensagem': 'Erro ao editar receita!'}
            return render(request, 'receitas/editar-receita.html', contexto)

class ReceitasDeleteView(View):
    def get(self, request, id, *args, **kwargs):
        receita = Receita.objects.get(id=id)
        contexto = {'receita': receita,
                    'titulo_pagina': 'Deletar',
                    'titulo_janela': 'Deletar Receita',
                    'botao': 'Deletar', }
        return render(request, 'receitas/deletar-receita.html', contexto)

    def post(self, request, id, *args, **kwargs):
        receita = Receita.objects.get(id=id)
        receita.delete()
        return HttpResponseRedirect(reverse_lazy("receitas:homepage"))

class VerReceita(View):
    def get(self, request, *args, **kwargs):
        receita = Receita.objects.get()
        contexto = { 'receita': receita,
                    'titulo_pagina': 'Ver receita',
                    'titulo_janela': 'Vendo receita',
            }
        return render(request,'receitas/ver_receita.html',contexto)
