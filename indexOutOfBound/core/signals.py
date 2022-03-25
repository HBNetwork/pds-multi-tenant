from django.dispatch import receiver

from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Tenant
from django.core.management import call_command

from django.conf import settings


@receiver(post_save, sender=Tenant)
def handle_tenant_created(sender, instance, created, **kwargs):
    if created:
        settings.DATABASES.update({
            instance.database_name: {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': settings.BASE_DIR / f'{instance.database_name}.db.sqlite3'
            }
        })

        call_command('migrate', database=instance.database_name)