"""
URL configuration for site_receitas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import include
from site_receitas import views

urlpatterns = [
    #seria bom renomear o admin ou excluir, porem sem esse path nao conseguimos acessar o django admin
    path("admin/", admin.site.urls, name = 'admin'),
    # Links para as URLs de receitas
    path('', include('receitas.urls', namespace='receitas')),
    # Links para as URLs de usuários
    path('', include('usuarios.urls', namespace='usuarios')),
    # Link para a página inicial de segurança
    path('seguranca/', views.homeSec, name='homeSec'),
    # Link para a página de registro
    path('seguranca/registro/', views.registro, name='sec-registro'),
]