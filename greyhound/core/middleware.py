import re
import threading

from django.conf import settings
from django.http import Http404

# from .models import Tenant

threadlocal = threading.local()


class NoTenant(Exception):
    ...


def split_tenant(path):
    if (match := re.search(r'/(.*?)(/.*)', path)):
        return match.groups()
    elif (match := re.search(r'/(.*)', path)):
        if (tenant := match.group(1)):
            return tenant, ''
    raise NoTenant(f'No tenant in {path}')


def tenant_available(tenant_name):
    from .models import Tenant
    # return Tenant.objects.filter(slug=tenant_name).exists()
    return Tenant.objects.filter(slug=tenant_name)


def tenant_exempt(tenant_name):
    return tenant_name in settings.TENANTS_EXEMPT


def current_tenant_name():
    # return getattr(threadlocal, 'tenant_id', None)
    try:
        return threadlocal.tenant_id
    except Exception as e:
        raise Exception(
            """
                Tenant is not set.
            """
        )


# def current_tenant():
#     tenant_name = current_tenant_name()
#     return Tenant.objects.get(slug=tenant_name)


def set_tenant_name(pk):
    threadlocal.tenant_id = pk


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant_name, path = self.get_tenant_from_url(request.path_info)

        if not tenant_exempt(tenant_name):
            self.check_tenant(tenant_name)
            request.tenant_name = tenant_name
            # threadlocal.tenant_name = tenant_name
            # set_tenant_name(tenant_name)
            request.path_info = path

        return self.get_response(request)

    @staticmethod
    def get_tenant_from_url(path):
        try:
            return split_tenant(path)
        except NoTenant:
            raise Http404()

    @staticmethod
    def check_tenant(tenant_name):
        tenant = tenant_available(tenant_name)
        # if not tenant_available(tenant_name):
        if not tenant.exists():
            raise Http404()
        set_tenant_name(tenant.first().id)