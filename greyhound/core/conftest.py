from pydoc import describe
import pytest
from core.models import Tenant, Operacao
from core.middleware import reset_tenant

@pytest.fixture
def exempt(settings):
    settings.TENANTS_EXEMPT = ['admin']
    return settings

@pytest.fixture
def tenant(request):
    return Tenant.objects.create(slug='tenant')

@pytest.fixture
def tenant0():
    return Tenant.objects.create(slug='tenant0')

@pytest.fixture
# @pytest.mark.parametrize('tenant', ('tenant', ))
def operacao(tenant):
    return Operacao.unscoped.create(tenant=tenant, descricao='Operação 1', valor=10)


@pytest.fixture
def threadlocal():
    reset_tenant()
    yield
    reset_tenant()