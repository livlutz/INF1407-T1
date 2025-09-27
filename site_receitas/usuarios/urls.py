
from django.contrib import admin
from django.urls import path
from usuarios import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy

# Define o namespace para as URLs do aplicativo de usuários
app_name = 'usuario'

# Define as rotas URL para o aplicativo de usuários
urlpatterns = [
    path('login/', views.login, name='login'), #rota de login
    path('cadastro/', views.UsuarioCreateView.as_view(), name='cadastro'), #rota de cadastro
    path('perfil/<int:id>/', views.perfil, name='perfil'), #rota de perfil
    path('deletar/<int:id>/', views.UsuarioDeleteView.as_view(), name='deletar'), #rota de deletar usuario
    path('perfil/atualizar/<int:id>/', views.UsuarioUpdateView.as_view(), name='atualizar_perfil'), #rota de atualizar perfil
    path('perfil/receitas/<int:id>/', views.ReceitaListView.as_view(), name='minhas_receitas'), #rota de receitas do usuario
    path('logout/', views.logout_confirm, name='logout_confirm'), #rota de confirmação de logout
    path('logout/real/', LogoutView.as_view(next_page=reverse_lazy('receitas:homepage')), name='logout'), #rota de logout
    path('password_change_form/<int:id>/', PasswordChangeView.as_view(template_name='usuarios/password_change_form.html',
                                                                    success_url=reverse_lazy('usuarios:sec-password-change-done', kwargs={'id': id})),
                                                                    name='sec-password-change'), #rota de mudança de senha
    path('password_change_done/<int:id>/', PasswordChangeDoneView.as_view(template_name='usuarios/password_change_done.html'), name='sec-password-change-done'), #rota de mudança de senha concluída
    path('perfil/ver_receitas/<int:id>/', views.ReceitaListView.as_view(), name='ver_minhas_receitas'), #rota de ver receitas do usuario
]