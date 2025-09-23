
from django.contrib import admin
from django.urls import path
from usuarios import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy

app_name = 'usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.UsuarioCreateView.as_view(), name='cadastro'),
    path('perfil/<int:id>/', views.perfil, name='perfil'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('perfil/atualizar/<int:id>/', views.UsuarioUpdateView.as_view(), name='atualizar_perfil'),
    path('perfil/receitas/<int:id>/', views.ReceitaListView.as_view(), name='minhas_receitas'),
    path('logout/', views.logout_confirm, name='logout_confirm'),
    path('logout/real/', LogoutView.as_view(next_page=reverse_lazy('receitas:homepage')), name='logout'),
    path('password_change_form/', PasswordChangeView.as_view(template_name='password_change_form.html', success_url=reverse_lazy('sec-password-change-done')), name='sec-password-change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='sec-password-change-done'),
]