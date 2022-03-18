from django.db import connection


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
