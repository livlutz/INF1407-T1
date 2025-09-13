from django.shortcuts import render
from django.http import HttpResponse
from receitas.models import Receita
from django.views.generic.base import View

# Create your views here.

#filtro ta com problema
class PubReceitasListView(View):
    def get(self, request, *args, **kwargs):
        pub_receitas = Receita.objects.all() #.filter(visibilidade='Pub').order_by('-id')
        contexto = { 'pub_receitas': pub_receitas, }
        return render(
            request,
            'receitas/home.html',
            contexto)

class VerReceita(View):
    def get(self, request, *args, **kwargs):
        receita = Receita.objects.all()
        contexto = { 'receita': receita, }
        return render(
            request,
            'receitas/ver-receita.html',
            contexto)
