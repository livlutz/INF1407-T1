from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from receitas.models import Receita
from django.views.generic.base import View
from usuarios.models import Usuario
from receitas.forms import ReceitaModel2Form
from django.urls.base import reverse_lazy
from django.http.response import HttpResponseRedirect

# Create your views here.

class ReceitasCreateView(View):
    """View que cria uma nova receita"""

    def get(self, request, *args, **kwargs):
        """ Renderiza o formulario para criar uma nova receita"""

        contexto = {'formulario': ReceitaModel2Form,
                    'titulo_pagina': 'Criar Receita',
                    'titulo_janela': 'Criar Nova Receita',
                    'botao': 'Criar Receita', }
        return render(request, 'receitas/criarReceita.html', contexto)


    def post(self, request, *args, **kwargs):
        """ Processa o formulario para criar uma nova receita"""

        formulario = ReceitaModel2Form(request.POST, request.FILES)
        if formulario.is_valid():
            receita = formulario.save(commit=False)
            receita = formulario.save(commit=False)
            receita.autor = request.user
            receita.save()
            return HttpResponseRedirect(reverse_lazy("receitas:homepage"))
        else:
            contexto = {'formulario': formulario,'mensagem': 'Erro ao criar receita!'}
            return render(request, 'receitas/criarReceita.html', contexto)

class PubReceitasListView(View):
    """View que lista as receitas públicas"""

    def get(self, request, *args, **kwargs):
        """ Renderiza a lista de receitas públicas"""

        receitas = Receita.objects.filter(visibilidade='pub') #TODO: filtro ta com problema
        contexto = {
            'pub_receitas': receitas,
            'titulo_janela': 'Receitas Públicas',
            'titulo_pagina': 'Homepage - Receitas',
        }
        return render(request, 'receitas/home.html', contexto)

class ReceitasUpdateView(View):
    """View que atualiza uma receita"""

    def get(self, request, id, *args, **kwargs):
        """ Renderiza o formulario para atualizar a receita"""

        receita = get_object_or_404(Receita, id=id)
        formulario = ReceitaModel2Form(instance=receita)
        contexto = {'formulario': formulario,
                    'titulo_pagina': 'Editar',
                    'titulo_janela': 'Editar Receita',
                    'botao': 'Salvar', }
        return render(request, 'receitas/atualizaReceita.html', contexto)

    def post(self, request, id, *args, **kwargs):
        """ Processa o formulario para atualizar a receita"""

        receita = get_object_or_404(Receita, id=id)
        formulario = ReceitaModel2Form(request.POST, request.FILES, instance=receita)

        if formulario.is_valid():
            receita = formulario.save()
            return HttpResponseRedirect(reverse_lazy("receitas:homepage"))

        else:
            contexto = {'formulario': formulario,'mensagem': 'Erro ao editar receita!'}
            return render(request, 'receitas/atualizaReceita.html', contexto)

class ReceitasDeleteView(View):
    """View que deleta uma receita"""

    def get(self, request, id, *args, **kwargs):
        """ Renderiza a confirmação para deletar a receita"""

        receita = get_object_or_404(Receita, id=id)
        contexto = {'receita': receita,
                    'titulo_pagina': 'Deletar',
                    'titulo_janela': 'Deletar Receita',
                    'botao': 'Deletar', }

        return render(request, 'receitas/deletaReceita.html', contexto)

    def post(self, request, id, *args, **kwargs):
        """ Processa a confirmação para deletar a receita"""

        receita = get_object_or_404(Receita, id=id)
        receita.delete()
        return HttpResponseRedirect(reverse_lazy("receitas:homepage"))

class VerReceita(View):
    """View que exibe os detalhes de uma receita"""

    def get(self, request,id, *args, **kwargs):
        """ Renderiza os detalhes da receita"""
        
        receita = get_object_or_404(Receita, pk=self.kwargs['id'])
        contexto = { 'receita': receita,
                    'titulo_pagina': 'Ver receita',
                    'titulo_janela': 'Vendo receita',
            }
        return render(request,'receitas/ver_receita.html',contexto)
