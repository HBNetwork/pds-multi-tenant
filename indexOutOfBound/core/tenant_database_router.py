from indexOutOfBound.core.middlewares import TenantMiddleware


class TenantRouter:
    def db_for_read(self, model, **hints):
        # request = TenantMiddleware.get_current_request()
        # key = self.get_database_key(request)  # Implement get_database_key
        # return key
        return 'tenant1'


    def db_for_write(self, model, **hints):
        return 'tenant1'
