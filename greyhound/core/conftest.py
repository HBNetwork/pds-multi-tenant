from pydoc import describe
import pytest
from core.models import Tenant, Operacao

@pytest.fixture
def tenant(settings):
    tenant = Tenant.objects.create(slug='tenant')
    tenant1 = Tenant.objects.create(slug='tenant1')
    tenant2 = Tenant.objects.create(slug='tenant2')
    operacao = Operacao.unscoped.create(tenant=tenant, descricao='Operação 1', valor=10)

    settings.TENANTS_EXEMPT = ['admin']
    return settings
