from django.db import connection
from django.db.utils import ProgrammingError

from update_sem_where.core.models import Schema


class DuplicatedSchemaError(Exception):
    pass


def create(name):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE SCHEMA {name}")
    except ProgrammingError as e:
        raise DuplicatedSchemaError(e) from e


def list():
    return Schema.objects.tenants()


def from_path(path):
    _, tenant, *_ = path.split('/')
    return tenant
