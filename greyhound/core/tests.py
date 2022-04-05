import pytest

from core.middleware import split_tenant, NoTenant

pytestmark = pytest.mark.django_db


def test_split_tenant(tenant):
    assert split_tenant('/tenant/') == ('tenant', '/')
    assert split_tenant('/tenant') == ('tenant', '')
    assert split_tenant('/tenant/saldo/') == ('tenant', '/saldo/')
    assert split_tenant('/tenant/saldo') == ('tenant', '/saldo')


def test_split_tenant_with_no_tenant(subtests):
    for path in ['', '/']:
        with subtests.test('should raises', path=path):
            pytest.raises(NoTenant,split_tenant, path=path)


def test_no_tenant(client):
    response = client.get('/')
    assert response.status_code == 404


def test_tenant_on_path(client, tenant):
    response = client.get('/tenant/')
    assert response.status_code == 200
    assert response.context['request'].tenant_name == 'tenant'


def test_tenant_with_append_slash(client, tenant):
    response = client.get('/tenant', follow=True)
    assert response.status_code == 200


def test_tenant_does_not_exist(client):
    response = client.get('/zezinho/')
    assert response.status_code == 404


def test_tenant_exempts(client):
    response = client.get('/admin/', follow=True)
    request = response.context.get('request')
    with pytest.raises(AttributeError):
        getattr(request, 'tenant_name')


def test_saldo_view(client, tenant):
    response = client.get('/tenant/saldo/')
    assert response.status_code == 200
    assert response.context['saldo'] == 10


def test_saldo_zero_view(client, tenant):
    response = client.get('/tenant1/saldo/')
    assert response.status_code == 200
    assert response.context['saldo'] == 0