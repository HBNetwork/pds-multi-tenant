import threading

from core.models import Tenant

THREAD_LOCAL = threading.local()

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant = self.tenant_from_request(request)

        if self.tenant_exists_on_db(tenant):
            request.tenant = tenant
            set_db_for_router(tenant)
        else:
            set_db_for_router('default')

        return self.get_response(request)

    def tenant_from_request(self, request):
        if request.path.startswith('/tenants/'):
            return request.path.split('/')[2]
        return None

    def tenant_exists_on_db(self, tenant):
        try:
            Tenant.objects.using('default').get(name=tenant)
            return True
        except Tenant.DoesNotExist:
            return False

def get_current_db_name():
    return getattr(THREAD_LOCAL, "DB", None)


def set_db_for_router(db):
    setattr(THREAD_LOCAL, "DB", db)