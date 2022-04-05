from update_sem_where.core.database import DatabaseMapper


def test_get_item():
    default_db = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'multi_schema_db',
        'PASSWORD': 'secret',
    }

    mapper = DatabaseMapper(default_db)

    assert mapper['tenant1'] == {
        **default_db,
        'USER': 'tenant1',
    }


def test_get_item_with_user():
    default_db = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'multi_schema_db',
        'PASSWORD': 'secret',
        'USER': 'should_overwrite',
    }

    mapper = DatabaseMapper(default_db)

    assert mapper['tenant1'] == {
        **default_db,
        'USER': 'tenant1',
    }


def test_contains():
    mapper = DatabaseMapper({})

    assert 'tenant1' in mapper
    assert 'whatever' in mapper
