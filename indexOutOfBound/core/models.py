from django.core.management import call_command
from django.db import models

# Create your models here.


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    database_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id is None:
            call_command('migrate', database=self.database_name)
        super().save(*args, **kwargs)
