from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    CoreConfig is the configuration class for the 'core' application.
    This class is responsible for setting up application-specific
    configurations and registering the app with Django.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
