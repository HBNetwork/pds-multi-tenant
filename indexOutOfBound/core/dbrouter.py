from core.middlewares import get_current_db_name


class TenantRouter:
    def db_for_read(self, model, **hints):
        return get_current_db_name()

    def db_for_write(self, model, **hints):
        return get_current_db_name()

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Just migrate tenant model on default db
        if model_name == 'tenant' and db != 'default':
            return False
        return None