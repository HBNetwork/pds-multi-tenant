from update_sem_where.core.thread import local


def test_default_tenant():
    assert local.tenant is None
