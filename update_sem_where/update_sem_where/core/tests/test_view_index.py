from http import HTTPStatus

import pytest
from django.shortcuts import resolve_url
from pytest_django.asserts import assertTemplateUsed

from update_sem_where.core import tenants


@pytest.mark.django_db
def test_status_code(client):
    response = client.get(resolve_url('index'))
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_template(client):
    response = client.get(resolve_url('index'))
    assertTemplateUsed(response, 'index.html')


@pytest.mark.django_db
def test_list_tenants(client):
    tenants.create('tenant1')
    tenants.create('tenant2')

    response = client.get(resolve_url('index'))

    assert 'tenant1' in str(response.content)
    assert 'tenant2' in str(response.content)


@pytest.mark.django_db
def test_list_tenants_with_href(client):
    tenants.create('tenant3')
    tenants.create('tenant4')

    response = client.get(resolve_url('index'))

    assert 'href="/tenant3"' in str(response.content)
    assert 'href="/tenant4"' in str(response.content)


@pytest.mark.django_db
def test_get_tenant(client):
    response = client.get('/tenant1', follow=True)
    assert 'Hello World, tenant1' in str(response.content)
