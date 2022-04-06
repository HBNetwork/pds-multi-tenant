from update_sem_where.core.middlewares import TenantMiddleware
from update_sem_where.core.thread import local


def test_set_tenant(rf):
    request = rf.get('/tenant1/')

    def get_response(request):
        pass

    middleware = TenantMiddleware(get_response)
    middleware(request)

    assert local.tenant == 'tenant1'
