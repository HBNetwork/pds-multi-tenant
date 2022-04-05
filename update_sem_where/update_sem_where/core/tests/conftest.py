import pytest

from update_sem_where.core.thread import local


@pytest.fixture(autouse=True)
def clear_thread():
    local.tenant = None
