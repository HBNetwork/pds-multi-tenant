from django.contrib.auth.models import AbstractUser
from django.db import models

from update_sem_where.core.managers import SchemaManager


class User(AbstractUser):
    pass


class Schema(models.Model):
    oid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, db_column='nspname')
    nspowner = models.IntegerField()
    nspacl = models.CharField(max_length=255)

    objects = SchemaManager()

    class Meta:
        managed = False
        db_table = 'pg_namespace'
