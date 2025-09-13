
from django.contrib import admin
from django.urls import path
from receitas import views 

#app_name = 'receitas'

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('<int:id>/', views.home, name= 'homepage_id'), # Não sei se funciona assim

]