
from django.contrib import admin
from django.urls import path
from usuarios import views 

#app_name = 'usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/<int:id>/', views.perfil, name='perfil'),
]