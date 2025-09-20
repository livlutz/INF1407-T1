
from django.contrib import admin
from django.urls import path
from receitas import views

app_name = 'receitas'

urlpatterns = [
    path('', views.PubReceitasListView.as_view(), name = 'homepage'),
    path('receita/<int:id>/', views.VerReceita.as_view(), name = 'ver_receita'),
]