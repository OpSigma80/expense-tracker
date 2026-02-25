from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    
    def ready(self):
        # Esta línea es la que conecta el "cable" del sistema automático
        import home.signals
