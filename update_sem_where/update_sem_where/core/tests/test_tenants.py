import pytest
from django.db import connection

from update_sem_where.core import tenants


@pytest.mark.django_db
def test_list_empty():
    assert tenants.list() == []


@pytest.mark.django_db
def test_list_one():
    tenant = 'tenant1'

    with connection.cursor() as cursor:
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {tenant}")

    assert tenants.list() == [tenant]


@pytest.mark.django_db
def test_list_multiple():
    tenant1, tenant2 = 'tenant1', 'tenant2'

    with connection.cursor() as cursor:
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {tenant1}")
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {tenant2}")

    assert tenants.list() == [tenant1, tenant2]

