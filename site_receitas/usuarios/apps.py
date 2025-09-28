from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    """Configuração da aplicação de usuários."""
    
    default_auto_field = "django.db.models.BigAutoField"
    name = "usuarios"
