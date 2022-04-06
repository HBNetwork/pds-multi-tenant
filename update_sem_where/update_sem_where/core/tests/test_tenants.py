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


@pytest.mark.django_db
def test_create():
    tenant = 'tenant'

    tenants.create(tenant)

    assert tenants.list() == [tenant]


@pytest.mark.django_db
def test_create_duplicated_raises_exception():
    tenant = 'tenant'

    tenants.create(tenant)

    with pytest.raises(tenants.DuplicatedSchemaError) as error:
        tenants.create(tenant)

    assert str(error.value) == f'schema "{tenant}" already exists\n'


@pytest.mark.django_db
def test_create_user():
    tenant = 'tenant'

    tenants.create(tenant)
    tenants.create_user(tenant)

    with connection.cursor() as cursor:
        cursor.execute("SELECT usename AS role_name FROM pg_catalog.pg_user;")
        users = cursor.fetchall()

    assert any(u[0] == tenant for u in users)


def test_from_path(rf):
    assert tenants.from_path('/tenant1/') == 'tenant1'
    assert tenants.from_path('/passaporte/') == 'passaporte'
    assert tenants.from_path('/passaporte2') == 'passaporte2'
    assert tenants.from_path('/tenant2/whatever') == 'tenant2'
