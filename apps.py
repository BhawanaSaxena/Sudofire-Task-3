from django.apps import AppConfig


default_app_config = "api1.apps.Ap1Config"

class Api1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api1'

    def ready(self):
        import api1.signals
