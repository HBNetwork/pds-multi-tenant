from update_sem_where.core.thread import local


class DatabaseMapper(dict):
    def __init__(self, default):
        self.cache = {'default': default}

    def __getitem__(self, item):
        if item not in self.cache:
            self.cache[item] = {
                **self.cache['default'],
                'USER': item,
            }
        return self.cache[item]

    def __contains__(self, item):
        return True


class DatabaseRouter:
    def db_for_read(self, *args, **hints):
        return local.tenant

    def db_for_write(self, *args, **hints):
        return local.tenant

    def allow_relation(self, *args, **hints):
        return True

    def allow_migrate(self, *args, **hints):
        return True
