from django.apps import AppConfig

from django.conf import settings


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        import core.signals
        from core.models import Tenant
        tenants = Tenant.objects.all()

        for tenant in tenants:
            settings.DATABASES.update({tenant.database_name: {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': settings.BASE_DIR / f'{tenant.database_name}.db.sqlite3'
            }})
