from django.conf import settings
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


def create_user(name):
    password = settings.DATABASES['default']['PASSWORD']
    username, schema = name, name

    sql = f"""
    CREATE USER {username} WITH LOGIN PASSWORD '{password}';
    ALTER ROLE {username} SET search_path TO {schema};
    """

    with connection.cursor() as cursor:
        cursor.execute(sql)


# def create(name):
#     create_schema(name)
#     create_user(name)


def delete_user(name):
    with connection.cursor() as cursor:
        cursor.execute(f"DROP ROLE IF EXISTS {name};")


def list():
    return Schema.objects.tenants()


def from_path(path):
    _, tenant, *_ = path.split('/')
    return tenant
