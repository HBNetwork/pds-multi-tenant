from django.db import connection
from django.db.utils import ProgrammingError


class DuplicatedSchemaError(Exception):
    pass


def create(name):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE SCHEMA {name}")
    except ProgrammingError as e:
        raise DuplicatedSchemaError(e) from e


def list():
    query = """
        SELECT
            nspname
        FROM
            pg_catalog.pg_namespace
        WHERE
            nspname !~ '(^pg_|information_schema|public)'
    """

    with connection.cursor() as cursor:
       cursor.execute(query)
       results = cursor.fetchall()

    return [r[0] for r in results]
