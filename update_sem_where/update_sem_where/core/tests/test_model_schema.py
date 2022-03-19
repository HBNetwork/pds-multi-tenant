import pytest

from update_sem_where.core import tenants
from update_sem_where.core.models import Schema


@pytest.mark.django_db
def test_query_all():
    schemas = Schema.objects.all()

    assert [s.name for s in schemas] == [
        'pg_toast', 'pg_catalog', 'public', 'information_schema'
    ]


@pytest.mark.django_db
def test_tenants():
    tenant = 'new_tenant'
    tenants.create(tenant)

    assert Schema.objects.tenants() == [tenant]
