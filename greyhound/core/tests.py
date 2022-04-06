import pytest

from core.middleware import split_tenant, NoTenant, current_tenant

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


def test_tenant_on_index(client, tenant):
    response = client.get('/tenant/')
    assert response.status_code == 200
    assert current_tenant() == tenant
    html = response.content.decode()
    assert '/tenant/saldo/' in html


def test_tenant_with_append_slash(client, tenant):
    response = client.get('/tenant', follow=True)
    assert response.status_code == 200


def test_tenant_does_not_exist(client):
    response = client.get('/zezinho/')
    assert response.status_code == 404


def test_saldo_view(client, operacao):
    response = client.get('/tenant/saldo/')
    assert response.status_code == 200
    assert response.context['saldo'] == 10


def test_tenants_exempt(client, threadlocal, settings):
    settings.TENANTS_EXEMPT = ['admin']

    response = client.get('/admin/', follow=True)
    request = response.context.get('request')
    with pytest.raises(NoTenant):
        current_tenant()


def test_inexistent_tenant_exempt(client, threadlocal):
    response = client.get('/admin/', follow=True)
    request = response.context.get('request')
    assert response.status_code == 404


# @pytest.mark.parametrize('tenant', ('tenant0', ))
def test_saldo_zero_view(client, tenant0):
    response = client.get('/tenant0/saldo/')
    assert response.status_code == 200
    assert response.context['saldo'] == 0