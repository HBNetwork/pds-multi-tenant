from http import HTTPStatus

from django.shortcuts import resolve_url
from pytest_django.asserts import assertTemplateUsed


def test_status_code(client):
    response = client.get(resolve_url('index'))
    assert response.status_code == HTTPStatus.OK


def test_template(client):
    response = client.get(resolve_url('index'))
    assertTemplateUsed(response, 'index.html')
