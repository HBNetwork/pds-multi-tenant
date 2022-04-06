from update_sem_where.core.database import DatabaseRouter
from update_sem_where.core.thread import local


def test_db_for_read():
    local.tenant = 'passaporte'
    assert DatabaseRouter().db_for_read() == 'passaporte'


def test_db_for_write():
    local.tenant = 'dev'
    assert DatabaseRouter().db_for_write() == 'dev'


def test_allow_relation():
    assert DatabaseRouter().allow_relation() is True


def test_allow_migrate():
    assert DatabaseRouter().allow_migrate() is True
