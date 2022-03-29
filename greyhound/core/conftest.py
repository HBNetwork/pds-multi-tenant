import pytest


@pytest.fixture
def tenant(settings):
    settings.TENANTS = ['tenant']
    settings.TENANTS_EXEMPT = ['admin']
    return settings
