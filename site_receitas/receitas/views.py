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
        return render(request, 'receitas/criarReceita.html', contexto)

    def post(self, request, *args, **kwargs):
        formulario = ReceitaModel2Form(request.POST, request.FILES)
        if formulario.is_valid():
            receita = formulario.save(commit=False)
            receita.autor = request.user
            receita.save()
            return HttpResponseRedirect(reverse_lazy("receitas:homepage"))
        else:
            contexto = {'formulario': formulario,'mensagem': 'Erro ao criar receita!'}
            return render(request, 'receitas/criarReceita.html', contexto)


class PubReceitasListView(View):
    def get(self, request, *args, **kwargs):
        receitas = Receita.objects.filter(visibilidade='pub')
        contexto = {
            'pub_receitas': receitas,
            'titulo_janela': 'Receitas Públicas',
            'titulo_pagina': 'Homepage - Receitas',
        }
        return render(request, 'receitas/home.html', contexto)

class ReceitasUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        receita = get_object_or_404(Receita, id=id)  # Fixed: Use get_object_or_404
        formulario = ReceitaModel2Form(instance=receita)
        contexto = {'formulario': formulario,
                    'titulo_pagina': 'Editar',
                    'titulo_janela': 'Editar Receita',
                    'botao': 'Salvar', }
        return render(request, 'receitas/atualizaReceita.html', contexto)

    def post(self, request, id, *args, **kwargs):
        receita = get_object_or_404(Receita, id=id)
        formulario = ReceitaModel2Form(request.POST, request.FILES, instance=receita)  # Fixed: Added request.FILES
        if formulario.is_valid():
            receita = formulario.save()
            return HttpResponseRedirect(reverse_lazy("receitas:homepage"))
        else:
            contexto = {'formulario': formulario,'mensagem': 'Erro ao editar receita!'}
            return render(request, 'receitas/atualizaReceita.html', contexto)

class ReceitasDeleteView(View):
    def get(self, request, id, *args, **kwargs):
        receita = get_object_or_404(Receita, id=id)  # Fixed: Use get_object_or_404
        contexto = {'receita': receita,
                    'titulo_pagina': 'Deletar',
                    'titulo_janela': 'Deletar Receita',
                    'botao': 'Deletar', }
        return render(request, 'receitas/deletaReceita.html', contexto)

    def post(self, request, id, *args, **kwargs):
        receita = get_object_or_404(Receita, id=id)  # Fixed: Use get_object_or_404
        receita.delete()
        return HttpResponseRedirect(reverse_lazy("receitas:homepage"))

class VerReceita(View):
    def get(self, request,id, *args, **kwargs):
        receita = get_object_or_404(Receita, id=id)
        contexto = { 'receita': receita,
                    'titulo_pagina': 'Ver receita',
                    'titulo_janela': 'Vendo receita',
            }
        return render(request,'receitas/ver_receita.html',contexto)
