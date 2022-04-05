from update_sem_where.core import tenants
from update_sem_where.core.thread import local


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        local.tenant = tenants.from_path(request.path)
        return self.get_response(request)
