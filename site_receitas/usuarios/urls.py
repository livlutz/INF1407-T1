
from django.contrib import admin
from django.urls import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.UsuarioCreateView.as_view(), name='cadastro'),
    path('perfil/<int:id>/', views.Perfil.as_view(), name='perfil'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('perfil/atualizar/<int:id>/', views.UsuarioUpdateView.as_view(), name='atualizar_perfil'),
    path('perfil/receitas/<int:id>/', views.ReceitaListView.as_view(), name='minhas_receitas'),
]